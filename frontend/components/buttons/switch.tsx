import { useState } from 'react';
import { View, Pressable } from 'react-native';

export default function Switch() {
    const [isEnabled, setIsEnabled] = useState(false);

    const toggleSwitch = () => setIsEnabled(previousState => !previousState);

    return (
        <View className="flex-1 items-center justify-center flex-row space-x-4">
            <Pressable
                onPress={toggleSwitch}
                className={`w-16 h-8 rounded-full justify-center px-1 transition-colors ${
                    isEnabled ? 'bg-indigo-300' : 'bg-slate-300'
                }`}
            >
                <View
                    className={`w-6 h-6 rounded-full bg-white transition-transform ${
                        isEnabled ? 'self-end' : 'self-start'
                    }`}
                />
            </Pressable>
        </View>
    );
}