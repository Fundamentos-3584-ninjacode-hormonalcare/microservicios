package com.backend.hormonalcare.communication.application.internal.outboundservices.acl;

import org.springframework.stereotype.Service;

@Service
public class CommunicationExternalProfileService {
    // Dummy implementation for microservice separation
    public boolean profileExists(Long profileId) {
        // TODO: Replace with REST call to IAM microservice
        return true; // Simula que el perfil existe
    }

    public String getProfileName(Long profileId) {
        // TODO: Replace with REST call to IAM microservice
        return "Dummy User"; // Simula un nombre de usuario
    }

    public String getProfileImage(Long profileId) {
        // TODO: Replace with REST call to IAM microservice
        return "https://dummyimage.com/profile.png"; // Simula una URL de imagen
    }
}