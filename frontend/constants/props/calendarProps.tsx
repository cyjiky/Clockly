export interface CalendarCreateProps {
    name: string;
    color: string;
}

export interface TimeLineProps {
    start_date: Date;
    end_date: Date;
}

export interface DateTimeObjProps extends TimeLineProps {
    name: string;
    description: string;
}

// TODO -> repeat days 
export interface EventProps extends DateTimeObjProps {
    repeat_days: string[] | null; 
}

export interface TaskProps extends DateTimeObjProps {
    completed: boolean;
}

export interface DayProps {
    date: Date;
    dayName: string;
    dayNumber: number;
    dayTask: TaskProps[];
    dayEvent: EventProps[];
    hasEvent?: boolean;
}

export interface WeekProps {
    weekStart: Date;
    weekEnd: Date;
    days: DayProps[];
}

export interface MonthProps {
    monthStart: Date;
    monthEnd: Date;
    weeks: WeekProps[];
}

export interface YearProps {
    yearStart: Date;
    yearEnd: Date;
    months: MonthProps[];
}