{
    "name": "Room Booking Management",
    "version": "1.0",
    "category": "Sales",  
    "summary": "Room bookings",
    "description": """
        test module
    """,
    "author": "Your Name",
    "website": "http://yourwebsite.com",
    "depends": ["base"],  
    "data": [
        "views/data.xml",
        "security/ir.model.access.csv",  
        "views/master_ruangan_views.xml",  
        "views/pemesanan_ruangan_views.xml",  
        "views/menu.xml",  
    ],
    "installable": True,  
    "application": True,  
    "auto_install": False,  
}
