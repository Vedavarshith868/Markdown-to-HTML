import markdown


def convert_md_to_html(md_content):
    body_content = markdown.markdown(
        md_content, extensions=["extra"]
    )  # Enables extra Markdown features

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        code {{ font-family: monospace; }}
    </style>
</head>
<body>
    {body_content}
</body>
</html>"""

    return html_content


# to test
# md_content = "This is a simple *Markdown* file. Markdown is a lightweight markup language that you can use to format text."
# print(convert_md_to_html(md_content))
