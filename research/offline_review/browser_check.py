#!/usr/bin/env python3
"""Offline browser smoke-test at real mobile/desktop widths, keyboard and print."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
PAGE = HERE / "human_review_offline.html"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        requests = []
        for width, height, name in ((390, 844, "mobile"), (1280, 900, "desktop")):
            page = browser.new_page(viewport={"width": width, "height": height},
                                    device_scale_factor=1)
            page.on("request", lambda request: requests.append(request.url))
            page.goto(PAGE.as_uri())
            page.wait_for_load_state("load")
            assert page.title().startswith("The Future Someone Can Actually Use")
            assert page.locator("main h3").count() == 10
            assert page.locator("main").is_visible()
            sizes = page.evaluate("""() => ({
                window: window.innerWidth,
                page: document.documentElement.scrollWidth,
                body: document.body.scrollWidth,
                main: document.querySelector('main').getBoundingClientRect().width,
                textSelect: getComputedStyle(document.querySelector('main p')).userSelect
            })""")
            assert sizes["page"] <= sizes["window"] + 1, (name, sizes)
            assert sizes["body"] <= sizes["window"] + 1, (name, sizes)
            assert sizes["main"] > 150, (name, sizes)
            assert sizes["textSelect"] != "none", (name, sizes)
            page.keyboard.press("Tab")
            focus = page.evaluate("document.activeElement.getAttribute('class')")
            assert focus == "skip", (name, focus)
            page.keyboard.press("Enter")
            assert page.evaluate("document.activeElement.id") == "main"
            # Real browser selectable text: use a DOM Range, no changes to the HTML.
            selection = page.evaluate("""() => {
                const p = document.querySelector('main p');
                const r = document.createRange(); r.selectNodeContents(p);
                const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
                return sel.toString().length;
            }""")
            assert selection > 40, (name, selection)
            assert all(url.startswith("file://") for url in requests), requests
            print(name, "PASS", sizes, "selection_length", selection,
                  "requests", len(requests))
            if name == "desktop":
                page.emulate_media(media="print")
                assert page.locator("nav").evaluate("(x) => getComputedStyle(x).display") == "none"
                # Exercise Chromium's actual print-to-PDF renderer, not just CSS inspection.
                pdf = page.pdf(format="A4", print_background=True)
                assert pdf.startswith(b"%PDF-") and len(pdf) > 25_000, len(pdf)
                print("print PASS, generated PDF bytes", len(pdf),
                      "(ephemeral QA only, not published or committed)")
            page.close()
        browser.close()


if __name__ == "__main__":
    main()
