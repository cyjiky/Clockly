import { View, Text } from 'react-native';

import { Avatario, AvatarFallback, AvatarImage } from '@/components/ui/avatar/avatario';

export default function Avatar() {
  return (
    <View className="flex-1 items-center justify-center">
        <Avatario alt="Zach Nugent's Avatar">
          <AvatarImage source={{ uri: 'https://github.com/mrzachnugent.png' }} />
          <AvatarFallback>
            <Text>ZN</Text>
          </AvatarFallback>
        </Avatario>
    </View>
  );
}