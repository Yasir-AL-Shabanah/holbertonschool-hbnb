from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # هذا السطر هو الذي ينشئ الجداول في قاعدة البيانات
        db.create_all()
        print("✅ Database tables created successfully.")
    
    app.run(debug=True)
