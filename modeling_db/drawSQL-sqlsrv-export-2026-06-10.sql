CREATE TABLE "student"(
    "student_code" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "student" ADD CONSTRAINT "student_student_code_primary" PRIMARY KEY("student_code");
CREATE TABLE "karname"(
    "id" INT NOT NULL,
    "student_code" INT NOT NULL,
    "type" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "karname" ADD CONSTRAINT "karname_id_primary" PRIMARY KEY("id");
CREATE TABLE "nomre"(
    "id" INT NOT NULL,
    "karname_id" INT NOT NULL,
    "class" VARCHAR(255) NOT NULL,
    "nomre" TINYINT NOT NULL
);
ALTER TABLE
    "nomre" ADD CONSTRAINT "nomre_id_primary" PRIMARY KEY("id");
CREATE TABLE "azmoon"(
    "id" INT NOT NULL,
    "grade" VARCHAR(255) NOT NULL,
    "time" VARCHAR(255) NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "head_nomre" INT NOT NULL,
    "teacher_id" INT NOT NULL
);
ALTER TABLE
    "azmoon" ADD CONSTRAINT "azmoon_id_primary" PRIMARY KEY("id");
CREATE TABLE "soal"(
    "id" INT NOT NULL,
    "azmoon_id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "is_did" VARBINARY(MAX) NOT NULL,
    "nomre" INT NOT NULL
);
ALTER TABLE
    "soal" ADD CONSTRAINT "soal_id_primary" PRIMARY KEY("id");
CREATE TABLE "gozine_soal"(
    "id" INT NOT NULL,
    "soal_id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "is_clicked" VARBINARY(MAX) NOT NULL
);
ALTER TABLE
    "gozine_soal" ADD CONSTRAINT "gozine_soal_id_primary" PRIMARY KEY("id");
CREATE TABLE "jajvab_azmoon"(
    "id" INT NOT NULL,
    "student_code" INT NOT NULL,
    "azmoon_id" INT NOT NULL,
    "nomre" INT NOT NULL
);
ALTER TABLE
    "jajvab_azmoon" ADD CONSTRAINT "jajvab_azmoon_id_primary" PRIMARY KEY("id");
CREATE TABLE "soal_javab"(
    "id" INT NOT NULL,
    "javab_azmoon_id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "is_did" VARBINARY(MAX) NOT NULL,
    "gozine" INT NOT NULL,
    "is_correct" VARBINARY(MAX) NOT NULL,
    "nomre" INT NOT NULL
);
ALTER TABLE
    "soal_javab" ADD CONSTRAINT "soal_javab_id_primary" PRIMARY KEY("id");
CREATE TABLE "teacher"(
    "teacher_code" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "lastname" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "teacher" ADD CONSTRAINT "teacher_teacher_code_primary" PRIMARY KEY("teacher_code");
CREATE TABLE "class"(
    "id" INT NOT NULL,
    "teacher_code" INT NOT NULL,
    "students" BIGINT NOT NULL
);
ALTER TABLE
    "class" ADD CONSTRAINT "class_id_primary" PRIMARY KEY("id");
CREATE TABLE "personel"(
    "persenel_code" INT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "lastname" VARCHAR(255) NOT NULL,
    "type" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "personel" ADD CONSTRAINT "personel_persenel_code_primary" PRIMARY KEY("persenel_code");
CREATE TABLE "news"(
    "id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "grade" VARCHAR(255) NOT NULL,
    "personel_id" INT NOT NULL
);
ALTER TABLE
    "news" ADD CONSTRAINT "news_id_primary" PRIMARY KEY("id");
CREATE TABLE "comments"(
    "id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "personel_id" INT NOT NULL
);
ALTER TABLE
    "comments" ADD CONSTRAINT "comments_id_primary" PRIMARY KEY("id");
CREATE TABLE "apcense"(
    "id" INT NOT NULL,
    "student_id" INT NOT NULL,
    "time" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "apcense" ADD CONSTRAINT "apcense_id_primary" PRIMARY KEY("id");
CREATE TABLE "apsence_reason"(
    "id" INT NOT NULL,
    "student_id" INT NOT NULL,
    "apsence_id" INT NOT NULL
);
ALTER TABLE
    "apsence_reason" ADD CONSTRAINT "apsence_reason_id_primary" PRIMARY KEY("id");
CREATE TABLE "homework"(
    "id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(MAX) NOT NULL,
    "class" VARCHAR(255) NOT NULL,
    "grade_id" INT NOT NULL
);
ALTER TABLE
    "homework" ADD CONSTRAINT "homework_id_primary" PRIMARY KEY("id");
CREATE TABLE "grade"(
    "id" INT NOT NULL,
    "student_id" INT NOT NULL,
    "teacher_id" INT NOT NULL
);
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_id_primary" PRIMARY KEY("id");
CREATE TABLE "rooidad"(
    "id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "time" VARCHAR(255) NOT NULL,
    "grade" INT NOT NULL
);
ALTER TABLE
    "rooidad" ADD CONSTRAINT "rooidad_id_primary" PRIMARY KEY("id");
CREATE TABLE "jashnvare"(
    "id" INT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "time" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "jashnvare" ADD CONSTRAINT "jashnvare_id_primary" PRIMARY KEY("id");
CREATE TABLE "ekhtar"(
    "id" INT NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "money" VARCHAR(255) NULL,
    "description" VARCHAR(255) NOT NULL,
    "student" INT NOT NULL
);
ALTER TABLE
    "ekhtar" ADD CONSTRAINT "ekhtar_id_primary" PRIMARY KEY("id");
ALTER TABLE
    "karname" ADD CONSTRAINT "karname_student_code_foreign" FOREIGN KEY("student_code") REFERENCES "student"("student_code");
ALTER TABLE
    "comments" ADD CONSTRAINT "comments_id_foreign" FOREIGN KEY("id") REFERENCES "personel"("persenel_code");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "student"("student_code");
ALTER TABLE
    "student" ADD CONSTRAINT "student_student_code_foreign" FOREIGN KEY("student_code") REFERENCES "grade"("student_id");
ALTER TABLE
    "soal_javab" ADD CONSTRAINT "soal_javab_javab_azmoon_id_foreign" FOREIGN KEY("javab_azmoon_id") REFERENCES "jajvab_azmoon"("id");
ALTER TABLE
    "rooidad" ADD CONSTRAINT "rooidad_grade_foreign" FOREIGN KEY("grade") REFERENCES "grade"("id");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_id_foreign" FOREIGN KEY("id") REFERENCES "grade"("id");
ALTER TABLE
    "gozine_soal" ADD CONSTRAINT "gozine_soal_soal_id_foreign" FOREIGN KEY("soal_id") REFERENCES "soal"("azmoon_id");
ALTER TABLE
    "apcense" ADD CONSTRAINT "apcense_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "student"("student_code");
ALTER TABLE
    "apsence_reason" ADD CONSTRAINT "apsence_reason_apsence_id_foreign" FOREIGN KEY("apsence_id") REFERENCES "apcense"("id");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_id_foreign" FOREIGN KEY("id") REFERENCES "azmoon"("grade");
ALTER TABLE
    "student" ADD CONSTRAINT "student_student_code_foreign" FOREIGN KEY("student_code") REFERENCES "class"("students");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_id_foreign" FOREIGN KEY("id") REFERENCES "homework"("grade_id");
ALTER TABLE
    "azmoon" ADD CONSTRAINT "azmoon_teacher_id_foreign" FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_code");
ALTER TABLE
    "jajvab_azmoon" ADD CONSTRAINT "jajvab_azmoon_azmoon_id_foreign" FOREIGN KEY("azmoon_id") REFERENCES "azmoon"("id");
ALTER TABLE
    "nomre" ADD CONSTRAINT "nomre_karname_id_foreign" FOREIGN KEY("karname_id") REFERENCES "karname"("id");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_teacher_id_foreign" FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_code");
ALTER TABLE
    "teacher" ADD CONSTRAINT "teacher_teacher_code_foreign" FOREIGN KEY("teacher_code") REFERENCES "grade"("teacher_id");
ALTER TABLE
    "jajvab_azmoon" ADD CONSTRAINT "jajvab_azmoon_student_code_foreign" FOREIGN KEY("student_code") REFERENCES "student"("student_code");
ALTER TABLE
    "grade" ADD CONSTRAINT "grade_id_foreign" FOREIGN KEY("id") REFERENCES "rooidad"("grade");
ALTER TABLE
    "class" ADD CONSTRAINT "class_students_foreign" FOREIGN KEY("students") REFERENCES "student"("student_code");
ALTER TABLE
    "apsence_reason" ADD CONSTRAINT "apsence_reason_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "student"("student_code");
ALTER TABLE
    "azmoon" ADD CONSTRAINT "azmoon_grade_foreign" FOREIGN KEY("grade") REFERENCES "grade"("id");
ALTER TABLE
    "homework" ADD CONSTRAINT "homework_grade_id_foreign" FOREIGN KEY("grade_id") REFERENCES "grade"("id");
ALTER TABLE
    "ekhtar" ADD CONSTRAINT "ekhtar_id_foreign" FOREIGN KEY("id") REFERENCES "student"("student_code");
ALTER TABLE
    "class" ADD CONSTRAINT "class_teacher_code_foreign" FOREIGN KEY("teacher_code") REFERENCES "teacher"("teacher_code");
ALTER TABLE
    "soal" ADD CONSTRAINT "soal_azmoon_id_foreign" FOREIGN KEY("azmoon_id") REFERENCES "azmoon"("id");
ALTER TABLE
    "news" ADD CONSTRAINT "news_grade_foreign" FOREIGN KEY("grade") REFERENCES "grade"("id");
ALTER TABLE
    "news" ADD CONSTRAINT "news_personel_id_foreign" FOREIGN KEY("personel_id") REFERENCES "personel"("persenel_code");
