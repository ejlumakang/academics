public class Student {
    private int studentNo;
    private String fname;
    private String lname;
    private String course;

    public Student()
    {
        studentNo = 0;
        fname = null;
        lname = null;
        course = null;
    }

    public int getStudentNo(){
        return this.studentNo; }
    public String getFname(){
        return this.fname; }
    public String getLname() {
        return this.lname; }
    public String getCourse() {
        return this.course; }

    public void setStudentNo(int StudentNo) {
        studentNo = StudentNo; }
    public void setFname(String first) {
        fname = first;
    }
    public void setLname(String last) {
        lname = last;
    }
    public void setCourse(String c) {
        course = c;
    }

    //Student Tester
    public static void main(String[] args) {
        Student s1 = new Student();

        s1.setFname("Juan ");
        s1.setLname("Dela Cruz\n");
        s1.setStudentNo(202012345);
        s1.setCourse("\nBSCS");
        System.out.println(s1.getFname() + s1.getLname() + s1.getStudentNo() + s1.getCourse());
    }
}