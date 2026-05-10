import React from 'react';
import { View } from 'react-native';
import CalendarNavbar from '@/components/navBar/calendarNavBar';
import type { CalendarScreenProps } from '@/constants/props/calendarProps';


export default function CalendarNavbarScreen({ 
    onNavigateToEventCard, 
    onNavigateToChangeCard,
    
}: CalendarScreenProps) {
    return (
        <View>
            <CalendarNavbar 
                onNavigateToEventCard={onNavigateToEventCard}
                onNavigateToChangeCard={onNavigateToChangeCard}
            />
        </View>
    )
}