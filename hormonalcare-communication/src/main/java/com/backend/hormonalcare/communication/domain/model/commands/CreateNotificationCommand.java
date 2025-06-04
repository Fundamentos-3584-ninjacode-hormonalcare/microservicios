package com.backend.hormonalcare.communication.domain.model.commands;

public class CreateNotificationCommand {
    private String title;
    private String message;
    private Enum<?> state;
    private Long recipientId;

    public CreateNotificationCommand(String title, String message, Enum<?> state, Long recipientId) {
        this.title = title;
        this.message = message;
        this.state = state;
        this.recipientId = recipientId;
    }

    // Getters and setters (opcional para dummy)
}
