export interface ActionButtonsProps {
    isOpen: boolean;
    onClose: () => void;
}

export interface ExtendedActionButtonsProps extends ActionButtonsProps {
    onSubmit?: () => void;
    isLoading?: boolean;
}