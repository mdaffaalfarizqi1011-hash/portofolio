from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # ✏️ GANTI: Nama lu
    name = "Muhammad Daffa Alfarizqi"

    # ✏️ GANTI: Stats singkat tentang lu
    stats = [
        {"value": "2th", "label": "Semester"},
        {"value": "10+", "label": "Proyek"},
        {"value": "3+", "label": "Tahun Coding"},
        {"value": "S1", "label": "Informatika"},
    ]

    # ✏️ GANTI: Skill lu — bisa tambah/hapus kategori dan item
    skills = {
        "Languages": ["Python", "JavaScript", "HTML", "CSS"],
        "Frameworks": ["Flask", "Bootstrap", "React"],
        "Tools": ["Git", "VS Code", "Figma", "Postman"],
    }

    # ✏️ GANTI: Proyek lu — isi title, desc, tag, dan link (boleh kosong "")
    projects = [
        {
            "tag": "Web · Flask",
            "title": "Proyek 1",
            "desc": "Deskripsi singkat proyek pertama lu. Apa yang dibuat, tech stack apa yang dipakai.",
            "link": "https://github.com/yourusername",
        },
        {
            "tag": "Web · React",
            "title": "Proyek 2",
            "desc": "Deskripsi singkat proyek kedua lu. Apa yang dibuat, tech stack apa yang dipakai.",
            "link": "",
        },
        {
            "tag": "Data · Python",
            "title": "Proyek 3",
            "desc": "Deskripsi singkat proyek ketiga lu. Apa yang dibuat, tech stack apa yang dipakai.",
            "link": "",
        },
    ]

    return render_template(
        'index.html',
        title=f"{name} — Portfolio",
        name=name,
        stats=stats,
        skills=skills,
        projects=projects,
    )


if __name__ == '__main__':
    app.run(debug=True)