def generate_links(data):
    platforms = ["facebook", "linkedin", "instagram", "tiktok", "youtube"]
    return [
        {
            "name": data[platform].replace("mailto:", "").replace("https://", ""),
            "link": data[platform]
        } for platform in platforms if data.get(platform)
    ]
