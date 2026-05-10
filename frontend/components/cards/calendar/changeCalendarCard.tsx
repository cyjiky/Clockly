import React, { useState } from 'react';
import { 
  View, 
  Text, 
  TouchableOpacity, 
  Modal, 
  ScrollView, 
  Switch 
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

import type { ExtendedActionButtonsProps } from '@/constants/props/internProps';
import { INITIAL_CALENDARS } from '@/constants/devConst';


export default function CalendarSelectionModal({ isOpen, onClose }: ExtendedActionButtonsProps) {
  const [calendars, setCalendars] = useState(INITIAL_CALENDARS);
  
  const [showDeclined, setShowDeclined] = useState(false);
  const [showCompleted, setShowCompleted] = useState(true);

  const toggleCalendar = (id: string) => {
    setCalendars(prev => 
      prev.map(cal => cal.id === id ? { ...cal, isChecked: !cal.isChecked } : cal)
    );
  };

  return (
    <Modal
      visible={isOpen}
      animationType="slide"
      presentationStyle="pageSheet"
      onRequestClose={onClose}
    >
      <View className="flex-1 bg-[#F2F2F7] pt-4">
        
        <View className="flex-row items-center justify-between px-4 pb-4">
          <TouchableOpacity 
            onPress={onClose} 
            activeOpacity={0.7}
            className="w-8 h-8 rounded-full bg-[#E5E5EA] items-center justify-center"
          >
            <Ionicons name="close" size={20} color="#8E8E93" />
          </TouchableOpacity>
          
          <Text className="text-black text-lg font-semibold">
            Calendars
          </Text>
          
          <View className="w-8" />
        </View>

        <ScrollView 
          className="flex-1 px-4" 
          showsVerticalScrollIndicator={false}
          contentContainerStyle={{ paddingBottom: 40 }}
        >
          
          <View className="flex-row justify-between items-center py-2 mt-4 mb-2">
            <Text className="text-black text-lg font-bold">iCloud</Text>
            <Ionicons name="chevron-down" size={20} color="#FF3B30" />
          </View>

          <View className="bg-white rounded-2xl overflow-hidden shadow-sm">
            {calendars.map((cal, index) => (
              <View key={cal.id}>
                <View className="flex-row items-center justify-between px-4 py-3.5">
                  
                  <TouchableOpacity 
                    onPress={() => toggleCalendar(cal.id)} 
                    activeOpacity={0.7}
                    className="flex-row items-center flex-1"
                  >
                    {cal.isChecked ? (
                      <Ionicons name="checkmark-circle" size={24} color={cal.color} />
                    ) : (
                      <View 
                        className="w-6 h-6 rounded-full border-2" 
                        style={{ borderColor: cal.color }} 
                      />
                    )}
                    <Text className="text-black text-[17px] ml-3">{cal.name}</Text>
                  </TouchableOpacity>

                  <TouchableOpacity activeOpacity={0.7} className="ml-4">
                    <Ionicons name="information-circle-outline" size={24} color="#FF3B30" />
                  </TouchableOpacity>
                  
                </View>

                {index < calendars.length - 1 && (
                  <View className="h-[0.5px] bg-[#E5E5EA] ml-[52px]" />
                )}
              </View>
            ))}
          </View>

          <View className="flex-row justify-between items-center py-4 mt-6">
            <Text className="text-[#8E8E93] text-[15px] font-medium uppercase">Other</Text>
            <Ionicons name="chevron-forward" size={20} color="#FF3B30" />
          </View>

          <View className="bg-white rounded-2xl overflow-hidden mb-6 shadow-sm">
            <View className="flex-row justify-between items-center px-4 py-3">
              <Text className="text-black text-[17px]">Rejected Events</Text>
              <Switch 
                value={showDeclined} 
                onValueChange={setShowDeclined} 
                trackColor={{ true: '#34C759', false: '#E9E9EA' }}
                ios_backgroundColor="#E9E9EA"
              />
            </View>
            
            <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />
            
            <View className="flex-row justify-between items-center px-4 py-3">
              <Text className="text-black text-[17px] w-[75%]">Show Completed Reminders</Text>
              <Switch 
                value={showCompleted} 
                onValueChange={setShowCompleted} 
                trackColor={{ true: '#34C759', false: '#E9E9EA' }}
                ios_backgroundColor="#E9E9EA"
              />
            </View>
          </View>

          <TouchableOpacity 
            activeOpacity={0.7}
            className="bg-white rounded-2xl flex-row items-center px-4 py-4 shadow-sm"
          >
            <Ionicons name="calendar-outline" size={22} color="#000000" />
            <Text className="text-black text-[17px] ml-3 font-medium">Add</Text>
          </TouchableOpacity>

        </ScrollView>
      </View>
    </Modal>
  );
}