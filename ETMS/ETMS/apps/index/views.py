from django.shortcuts import render


# Create your views here.


def index(request):
    """主页"""
    return render(request, "html/index.html")


def lesson(request):
    """课程安排"""
    return render(request, "html/lesson.html")


def classroom(request):
    """课程安排"""
    return render(request, "html/classroom.html")


def classes(request):
    """课程安排"""
    return render(request, "html/classes.html")


def attendance(request):
    """课程安排"""
    return render(request, "html/attendance.html")


def super_student(request):
    """课程安排"""
    return render(request, "html/super_student.html")


def super_teacher(request):
    """课程安排"""
    return render(request, "html/super_teacher.html")
