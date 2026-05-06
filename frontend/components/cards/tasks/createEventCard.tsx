import React, { useState } from 'react';
import type { EventProps } from '@/constants/props/calendarProps';
import type { ExtendedActionButtonsProps } from "@/constants/props/internProps";
import {
  View,
  Text,
  Alert,
  TextInput,
  TouchableOpacity,
  KeyboardAvoidingView,
  Platform,
  Switch,
  ScrollView,
  Modal,
  SafeAreaView
} from 'react-native';

import { API_URL } from '@/constants/api';

export default function CreateEventCard() {
    const [title, setTitle] = useState('');
    const [location, setLocation] = useState('');
    const [isAllDay, setIsAllDay] = useState(false);

    const [formData, setFormData] = useState<EventProps>({
        name: "",
        description: "",
        start_date: null,
        end_date: null,
        repeat_days: [""],
    });

    const [loading, setLoading] = useState(false);

    const handleChange = (field: keyof EventProps, value: string) => {
        let newValue: string | null = value;
        setFormData((prev) => ({ ...prev, [field]: newValue }));
    };

    const handleSubmit = async () => {
        if (!formData.name || !formData.description || !formData.start_date || !formData.end_date || !formData.repeat_days) {
            Alert.alert("Required Fields", "Please fill in all required event details.");
            return;
        }
        setLoading(true);
        try {
            const response = await fetch(`${API_URL}/`, { // TODO
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });
    
            if (!response.ok) {
                const errorBody = await response.json();
                throw new Error("Failed to create event");
            }
            // onClose();
        } catch (error) {
            Alert.alert("Error", "Event creation failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Modal
            transparent={true}
            animationType="slide"
            // visible={isOpen}
            // onRequestClose={handleClose}
        >
            <View className="flex-1 bg-black/40 justify-end">
                
                <View className="bg-[#F2F2F7] flex-1 mt-16 mx-3 mb-8 rounded-3xl overflow-hidden shadow-lg shadow-black/20">
                    <KeyboardAvoidingView
                        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
                        className="w-full flex-1"
                    >
                        {Platform.OS !== 'web' && (
                            <View className="items-center pt-4 pb-1">
                                <View className="w-12 h-1.5 bg-[#D1D1D6] rounded-full" />
                            </View>
                        )}

                        <ScrollView
                            showsVerticalScrollIndicator={false}
                            keyboardShouldPersistTaps="handled"
                            contentContainerStyle={{ paddingBottom: 40 }}
                        >
                            <View className="flex-row justify-between items-center px-5 pt-3 pb-4">
                                <TouchableOpacity activeOpacity={0.7}>
                                    <Text className="text-[#007AFF] text-lg">Cancel</Text>
                                </TouchableOpacity>

                                <Text className="text-black text-lg font-semibold">New Event</Text>
                                
                                <TouchableOpacity activeOpacity={0.7} onPress={handleSubmit}>
                                    <Text className="text-[#007AFF] text-lg font-semibold">Add</Text>
                                </TouchableOpacity>
                            </View>

                            <View className="bg-white rounded-2xl mx-4 mt-2 overflow-hidden shadow-sm">
                                <TextInput
                                    className="px-4 py-4 text-base text-black"
                                    placeholder="Title"
                                    placeholderTextColor="#8E8E93"
                                    value={formData.name}
                                    onChangeText={(text: string) => handleChange("name", text)}
                                />
                                <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />
                                <TextInput
                                    className="px-4 py-4 text-base text-black"
                                    placeholder="Location or Video Call"
                                    placeholderTextColor="#8E8E93"
                                    value={location}
                                    onChangeText={setLocation}
                                />
                            </View>

                            <View className="bg-white rounded-2xl mx-4 mt-6 overflow-hidden shadow-sm">
                                <View className="flex-row justify-between items-center px-4 py-3">
                                    <Text className="text-base text-black">All-day</Text>
                                    <Switch
                                        value={isAllDay}
                                        onValueChange={setIsAllDay}
                                        trackColor={{ true: '#34C759', false: '#E9E9EA' }}
                                    />
                                </View>

                                <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                                <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
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

                                <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                                <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
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

                            <View className="bg-white rounded-2xl mx-4 mt-6 overflow-hidden shadow-sm">
                                <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                                    <Text className="text-base text-black">Repeat</Text>
                                    <View className="flex-row items-center">
                                        <Text className="text-base text-[#8E8E93] mr-2">Never</Text>
                                        <Text className="text-[#C6C6C8] text-xl font-medium">›</Text>
                                    </View>
                                </TouchableOpacity>

                                <View className="h-[0.5px] bg-[#E5E5EA] ml-4" />

                                <TouchableOpacity activeOpacity={0.7} className="flex-row justify-between items-center px-4 py-3.5">
                                    <Text className="text-base text-black">Alert</Text>
                                    <View className="flex-row items-center">
                                        <Text className="text-base text-[#8E8E93] mr-2">10 minutes before</Text>
                                        <Text className="text-[#C6C6C8] text-xl font-medium">›</Text>
                                    </View>
                                </TouchableOpacity>
                            </View>

                            <View className="bg-white rounded-2xl mx-4 mt-6 mb-6 overflow-hidden shadow-sm">
                                <TextInput
                                    className="px-4 py-4 text-base text-black min-h-[120px]"
                                    placeholder="Description"
                                    placeholderTextColor="#8E8E93"
                                    multiline={true}
                                    textAlignVertical="top"
                                    value={formData.description}
                                    onChangeText={(text: string) => handleChange("description", text)}
                                />
                            </View>

                        </ScrollView>
                    </KeyboardAvoidingView>
                </View>
            </View>
        </Modal>
    );
}