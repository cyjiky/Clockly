import React, { useState } from 'react'
import { View } from 'react-native'

import CalendarHomeScreen from './calendarNavbarScreen';
import CreateEventCard from './createEventCard';
import ChangeCalendarCard from './changeCalendarCard';


export default function CalendarNavbarNavigate() {
    const [
        activeCard, setActiveCard
    ] = useState<'none' | 'createEvent' | 'changeCalendar'>('none');

    return (
        <View>

            <CalendarHomeScreen
                onNavigateToEventCard={() => setActiveCard('createEvent')}
                onNavigateToChangeCard={() => setActiveCard('changeCalendar')}
            />

            <CreateEventCard
                isOpen={activeCard === 'createEvent'}
                onClose={() => setActiveCard('none')}
            />
            
            <ChangeCalendarCard
                isOpen={activeCard === 'changeCalendar'}
                onClose={() => setActiveCard('none')}
            />

        </View>
    )
}