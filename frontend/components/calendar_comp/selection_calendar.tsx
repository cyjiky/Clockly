import React from 'react';
import { View } from 'react-native';
import { Picker, PickerItem } from '@/nativewindui/Picker';

// TODO 
// https://nativewindui.com/component/picker
export default function CalendarSelection() {
    const [picker, setPicker] = React.useState('blue');
    return (
        <View className="flex-1 items-center justify-center">
            <Picker selectedValue={picker} onValueChange={(itemValue) => setPicker(itemValue)}>
                <PickerItem
                    label="calendar 1"
                    value="1"
                    color="red"
                />
                <PickerItem
                    label="calendar 2"
                    value="2"
                    color="blue"
                />
                </Picker>
        </View>
    )
}