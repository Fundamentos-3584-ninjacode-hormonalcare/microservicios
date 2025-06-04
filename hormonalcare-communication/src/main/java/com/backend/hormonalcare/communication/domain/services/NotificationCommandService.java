package com.backend.hormonalcare.communication.domain.services;

import com.backend.hormonalcare.communication.domain.model.commands.CreateNotificationCommand;
import org.springframework.stereotype.Service;

@Service
public class NotificationCommandService {
    public void handle(CreateNotificationCommand command) {
        // Dummy: Aquí iría la lógica real o integración futura
    }
}
