students = [
    {"name": "sara", "age": 20, "university": "amirkabir"},
    {"name": "taha", "age": 21, "university": "tehran markaz"},
    {"name": "kiana", "age": 23, "university": "tehran"},
    {"name": "mohsen", "age": 26, "university": "elm va sanaat"},
]

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>People Info Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4b400;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>University</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>Software Engineer</td>
                <td>New York</td>
            </tr>
"""

# INJA FOR BEZANID

html += """
        </tbody>
    </table>
</body>
</html>
"""
