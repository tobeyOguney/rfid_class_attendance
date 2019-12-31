// @material-ui/icons
import Person from "@material-ui/icons/Person";
import Class from "@material-ui/icons/Class";
import ViewList from "@material-ui/icons/ViewList";

// core components/views for StudentAdmin layout
import StudentProfile from "views/UserProfile/StudentProfile.js";
import StudentCourses from "views/UserProfile/StudentCourses.js";

// core components/views for LecturerAdmin layout
import LecturerProfile from "views/UserProfile/LecturerProfile.js";
import LecturerCourses from "views/UserProfile/LecturerCourses.js";
import LecturerCourses from "views/UserProfile/LecturerCourses.js";
import LecturerAttendances from "views/UserProfile/LecturerAttendances.js";


studentDashboardRoutes = [
    {
        path: "/student/profile",
        name: "Profile",
        icon: Person,
        component: StudentProfile,
        layout: "/student/admin"
    },
    {
        path: "/student/courses",
        name: "Courses",
        icon: Class,
        component: StudentCourses,
        layout: "/student/admin"
    }
];

lecturerDashboardRoutes = [
    {
        path: "/lecturer/profile",
        name: "Profile",
        icon: Person,
        component: LecturerProfile,
        layout: "/lecturer/admin"
    },
    {
        path: "/lecturer/courses",
        name: "Courses",
        icon: Class,
        component: LecturerCourses,
        layout: "/lecturer/admin"
    },
    {
        path: "/lecturer/attendances",
        name: "Attendances",
        icon: ViewList,
        component: LecturerAttendances,
        layout: "/lecturer/admin"
    }
];

export default {studentDashboardRoutes, lecturerDashboardRoutes};
