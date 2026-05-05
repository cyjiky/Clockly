import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  KeyboardAvoidingView,
  Platform,
  Switch,
  ScrollView,
} from 'react-native';

// import { EventProps } from '@/constants/props/calendarProps';

// TODO 

export default function CreateEventCard() {
    const [title, setTitle] = useState('');
    const [location, setLocation] = useState('');
    const [isAllDay, setIsAllDay] = useState(false);

    // const [formData, setFormData] = useState<EventProps>({
    //     name: "",
    //     description: "",
    //     start_date: null,
    //     end_date: null,
    //     repeat_days: [""],
    // });

    return (
        <View className="flex-1 w-full h-full bg-[#F2F2F7] overflow-hidden">
            <KeyboardAvoidingView
                behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
                className="w-full flex-1"
            >
                {Platform.OS !== 'web' && (
                <View className="items-center pt-3 pb-2">
                    <View className="w-16 h-1.5 bg-slate-300 rounded-full" />
                </View>
                )}

            <ScrollView
                showsVerticalScrollIndicator={false}
                keyboardShouldPersistTaps="handled"
            >
            <View className="flex-row justify-between items-center px-4 pt-4 pb-2">
                <TouchableOpacity>
                    <Text className="text-[#007AFF] text-lg">Cancel</Text>
                </TouchableOpacity>

                <Text className="text-black text-lg font-semibold">New Event</Text>
                
                <TouchableOpacity>
                    <Text className="text-[#007AFF] text-lg font-semibold opacity-50">Add</Text>
                </TouchableOpacity>
            </View>

            <View className="bg-white rounded-xl mx-4 mt-6 overflow-hidden">
                <TextInput
                    className="px-4 py-3.5 text-base text-black"
                    placeholder="Title"
                    placeholderTextColor="#8E8E93"
                    value={title}
                    onChangeText={setTitle}
                />
                <View className="h-[0.5px] bg-[#C6C6C8] ml-4" />
                <TextInput
                    className="px-4 py-3.5 text-base text-black"
                    placeholder="Location or Video Call"
                    placeholderTextColor="#8E8E93"
                    value={location}
                    onChangeText={setLocation}
                />
            </View>

            <View className="bg-white rounded-xl mx-4 mt-6 overflow-hidden">
                
                <View className="flex-row justify-between items-center px-4 py-2">
                    <Text className="text-base text-black">All-day</Text>
                    <Switch
                        value={isAllDay}
                        onValueChange={setIsAllDay}
                        trackColor={{ true: '#34C759', false: '#E9E9EA' }}
                    />
                </View>

                <View className="h-[0.5px] bg-[#C6C6C8] ml-4" />

                <TouchableOpacity className="flex-row justify-between items-center px-4 py-3.5">
                    <Text className="text-base text-black">Starts</Text>
                    <View className="flex-row items-center gap-2">
                        <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                            May 5, 2026
                        </Text>
                        {!isAllDay && (
                        <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                            9:00 PM
                        </Text>
                        )}
                    </View>
                </TouchableOpacity>

                <View className="h-[0.5px] bg-[#C6C6C8] ml-4" />

                <TouchableOpacity className="flex-row justify-between items-center px-4 py-3.5">
                <Text className="text-base text-black">Ends</Text>
                <View className="flex-row items-center gap-2">
                    <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                        May 5, 2026
                    </Text>
                    {!isAllDay && (
                    <Text className="text-base text-black bg-[#F2F2F7] px-3 py-1.5 rounded-lg overflow-hidden">
                        10:00 PM
                    </Text>
                    )}
                </View>
                </TouchableOpacity>
            </View>

            <View className="bg-white rounded-xl mx-4 mt-6 overflow-hidden">
                <TouchableOpacity className="flex-row justify-between items-center px-4 py-3.5">
                <Text className="text-base text-black">Repeat</Text>
                <View className="flex-row items-center">
                    <Text className="text-base text-[#8E8E93] mr-2">Never</Text>
                    <Text className="text-[#C6C6C8] text-lg font-bold">›</Text>
                </View>
                </TouchableOpacity>

            <View className="h-[0.5px] bg-[#C6C6C8] ml-4" />

            <TouchableOpacity className="flex-row justify-between items-center px-4 py-3.5">
                <Text className="text-base text-black">Alert</Text>
                <View className="flex-row items-center">
                    <Text className="text-base text-[#8E8E93] mr-2">10 minutes before</Text>
                    <Text className="text-[#C6C6C8] text-lg font-bold">›</Text>
                </View>
            </TouchableOpacity>
          </View>

          <View className="flex-1 min-h-[32px]" />

        </ScrollView>
      </KeyboardAvoidingView>
    </View>
  );
}