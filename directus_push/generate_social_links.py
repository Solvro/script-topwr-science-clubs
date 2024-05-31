def generate_links(data):
    platforms = ["email", "facebook", "linkedin", "instagram", "tiktok", "youtube"]
    return [
        {
            "name": data[platform]
            .replace("mailto:", "")
            .replace("https://", "")
            .replace("http://", "")
            .replace("www.", ""),
            "link": data[platform],
        }
        for platform in platforms
        if data.get(platform)
    ]
