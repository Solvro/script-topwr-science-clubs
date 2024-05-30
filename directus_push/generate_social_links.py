def generate_links(data):
    platforms = ["facebook", "linkedin", "instagram", "tiktok", "youtube"]
    return [
        {
            "name": platform,
            "link": data[platform]
        } for platform in platforms if data.get(platform)
    ]
