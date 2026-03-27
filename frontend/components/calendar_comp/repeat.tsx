import { View, Text } from 'react-native';
import { Bold, Italic, Underline } from 'lucide-react-native';
import { ToggleGroup, ToggleGroupIcon, ToggleGroupItem } from '@/components/ui/toggle-group';
import * as React from 'react';

// TODO 

export default function Repeat() {
    const [value, setValue] = React.useState<string[]>([]);
    return (
        <View className="flex-1 items-center justify-center bg-slate-100">
            <ToggleGroup value={value} onValueChange={setValue} variant='outline' type='multiple'>
                <ToggleGroupItem isFirst value='bold' aria-label='Toggle bold'>
                    <ToggleGroupIcon as={Bold} />
                </ToggleGroupItem>
                <ToggleGroupItem value='italic' aria-label='Toggle italic'>
                    <ToggleGroupIcon as={Italic} />
                </ToggleGroupItem>
                <ToggleGroupItem isLast value='strikethrough' aria-label='Toggle strikethrough'>
                    <ToggleGroupIcon as={Underline} />
                </ToggleGroupItem>
            </ToggleGroup>
        </View>
    )
}
