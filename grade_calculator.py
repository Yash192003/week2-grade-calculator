{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "63f541ad-af35-4c89-8689-2d50fe2f342e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==================================================\n",
      "      STUDENT GRADE CALCULATOR\n",
      "==================================================\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number of students:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=== STUDENT 1 ===\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Student name:  Sarah Johnson\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter marks (0-100):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Math:  56\n",
      "Science:  67\n",
      "English:  78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=== STUDENT 2 ===\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Student name:  Raghava\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter marks (0-100):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Math:  89\n",
      "Science:  98\n",
      "English:  86\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=== STUDENT 3 ===\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Student name:  Manish\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter marks (0-100):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Math:  89\n",
      "Science:  99\n",
      "English:  78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==================================================\n",
      "            RESULTS SUMMARY\n",
      "==================================================\n",
      "Name                 |   Avg | Grade | Comment\n",
      "------------------------------------------------------------\n",
      "Sarah Johnson        |  67.0 |   D   | Needs Improvement. Please study more.\n",
      "Raghava              |  91.0 |   A   | Excellent! Keep up the great work!\n",
      "Manish               |  88.7 |   B   | Very Good! You're doing well.\n",
      "\n",
      "==================================================\n",
      "          CLASS STATISTICS\n",
      "==================================================\n",
      "Total Students: 3\n",
      "Class Average: 82.2\n",
      "Highest Average: 91.0 (Raghava)\n",
      "Lowest Average: 67.0 (Sarah Johnson)\n",
      "\n",
      "==================================================\n",
      "Thank you for using the Grade Calculator!\n",
      "==================================================\n"
     ]
    }
   ],
   "source": [
    "# Nallan Chakravathula Yashaswini\n",
    "# Student Grade Calculator\n",
    "# Week 2 Project - Control Flow & Data Structures\n",
    "# A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics.\n",
    "\n",
    "def calculate_grade(average):\n",
    "    \"\"\"Calculate grade based on average marks\"\"\"\n",
    "    if average >= 90:\n",
    "        return 'A', 'Excellent! Keep up the great work!'\n",
    "    elif average >= 80:\n",
    "        return 'B', 'Very Good! You\\'re doing well.'\n",
    "    elif average >= 70:\n",
    "        return 'C', 'Good. Room for improvement.'\n",
    "    elif average >= 60:\n",
    "        return 'D', 'Needs Improvement. Please study more.'\n",
    "    else:\n",
    "        return 'F', 'Failed. Please seek help from teacher.'\n",
    "\n",
    "def get_valid_number(prompt, min_val=0, max_val=100):\n",
    "    \"\"\"Get a valid number within specified range\"\"\"\n",
    "    while True:\n",
    "        try:\n",
    "            value = float(input(prompt))\n",
    "            if min_val <= value <= max_val:\n",
    "                return value\n",
    "            else:\n",
    "                print(f\"Please enter a number between {min_val} and {max_val}\")\n",
    "        except ValueError:\n",
    "            print(\"Invalid input! Please enter a number.\")\n",
    "\n",
    "def main():\n",
    "    print(\"=\" * 50)\n",
    "    print(\"      STUDENT GRADE CALCULATOR\")\n",
    "    print(\"=\" * 50)\n",
    "    print()\n",
    "    \n",
    "    # Get number of students with validation\n",
    "    while True:\n",
    "        try:\n",
    "            num_students = int(input(\"Enter number of students: \"))\n",
    "            if num_students > 0:\n",
    "                break\n",
    "            else:\n",
    "                print(\"Please enter a positive number!\")\n",
    "        except ValueError:\n",
    "            print(\"Invalid input! Please enter a whole number.\")\n",
    "    \n",
    "    # Initialize lists to store data\n",
    "    student_names = []\n",
    "    student_marks = []  # Will be list of lists\n",
    "    student_results = []  # Will store (average, grade, comment)\n",
    "    \n",
    "    # Collect data for each student\n",
    "    for i in range(num_students):\n",
    "        print(f\"\\n=== STUDENT {i+1} ===\")\n",
    "        \n",
    "        # Get student name\n",
    "        name = input(\"Student name: \")\n",
    "        while name.strip() == \"\":\n",
    "            print(\"Name cannot be empty!\")\n",
    "            name = input(\"Student name: \")\n",
    "        student_names.append(name)\n",
    "        \n",
    "        # Get marks for 3 subjects\n",
    "        print(\"Enter marks (0-100):\")\n",
    "        math = get_valid_number(\"Math: \")\n",
    "        science = get_valid_number(\"Science: \")\n",
    "        english = get_valid_number(\"English: \")\n",
    "        \n",
    "        # Store marks\n",
    "        student_marks.append([math, science, english])\n",
    "        \n",
    "        # Calculate average\n",
    "        average = (math + science + english) / 3\n",
    "        \n",
    "        # Get grade and comment\n",
    "        grade, comment = calculate_grade(average)\n",
    "        \n",
    "        # Store results\n",
    "        student_results.append({\n",
    "            'average': average,\n",
    "            'grade': grade,\n",
    "            'comment': comment\n",
    "        })\n",
    "    \n",
    "    # Display results\n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"            RESULTS SUMMARY\")\n",
    "    print(\"=\" * 50)\n",
    "    print(f\"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment\")\n",
    "    print(\"-\" * 60)\n",
    "    \n",
    "    for i in range(num_students):\n",
    "        name = student_names[i]\n",
    "        avg = student_results[i]['average']\n",
    "        grade = student_results[i]['grade']\n",
    "        comment = student_results[i]['comment']\n",
    "        \n",
    "        print(f\"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}\")\n",
    "    \n",
    "    # Calculate and display statistics\n",
    "    if num_students > 0:\n",
    "        averages = [result['average'] for result in student_results]\n",
    "        class_avg = sum(averages) / len(averages)\n",
    "        max_avg = max(averages)\n",
    "        min_avg = min(averages)\n",
    "        max_index = averages.index(max_avg)\n",
    "        min_index = averages.index(min_avg)\n",
    "        \n",
    "        print(\"\\n\" + \"=\" * 50)\n",
    "        print(\"          CLASS STATISTICS\")\n",
    "        print(\"=\" * 50)\n",
    "        print(f\"Total Students: {num_students}\")\n",
    "        print(f\"Class Average: {class_avg:.1f}\")\n",
    "        print(f\"Highest Average: {max_avg:.1f} ({student_names[max_index]})\")\n",
    "        print(f\"Lowest Average: {min_avg:.1f} ({student_names[min_index]})\")\n",
    "    \n",
    "    print(\"\\n\" + \"=\" * 50)\n",
    "    print(\"Thank you for using the Grade Calculator!\")\n",
    "    print(\"=\" * 50)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bc76d0d-678f-459e-b379-952563440ba1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
