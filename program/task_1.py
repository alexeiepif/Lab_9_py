#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    school = {
        '1а': 25,
        '1б': 27,
        '2б': 20,
        '6а': 30,
        '7в': 22
    }
    
    # а) изменилось количество учащихся в одном из классов
    school['1а'] = 26
    
    # б) появился новый класс
    school['8г'] = 18
    
    # в) расформирован (удален) другой класс
    del school['2б']
    
    total_students = sum(school.values())
    print("Общее количество учащихся в школе:", total_students)