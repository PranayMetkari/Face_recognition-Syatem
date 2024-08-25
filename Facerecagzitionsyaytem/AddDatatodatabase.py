import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-b2a65-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')


data = {
    "PKA000":
        {
            "name": "Pranay Metkari",
            "roll no": "B017",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "12",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA001":
        {
            "name": "Sanket Patade",
            "roll no": "B011",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "45",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA004":
        {
            "name": "Aditya Aeer",
            "roll no": "B021",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "35",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA005":
        {
            "name": "Kashish Borale",
            "roll no": "B010",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "9",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA006":
        {
            "name": "Ritvik Salian",
            "roll no": "B002",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "40",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA007":
        {
            "name": "Vedant Shimpi",
            "roll no": "B011",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "35",
            "last_Attendance_time": "2024-04-03 00:54:34"

        },
    "PKA008":
        {
            "name": "Ujwal Bagul",
            "roll no": "B011",
            "div": "B",
            "branch": "COMPS",
            "Year": "2",
            "total_Attendance": "35",
            "last_Attendance_time": "2024-04-03 00:54:34"

        }
}

for key,value in data.items():
    ref.child(key).set(value)
