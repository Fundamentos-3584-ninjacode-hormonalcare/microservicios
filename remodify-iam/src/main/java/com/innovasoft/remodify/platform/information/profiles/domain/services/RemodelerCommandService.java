package com.innovasoft.remodify.platform.information.profiles.domain.services;


import com.innovasoft.remodify.platform.information.profiles.domain.model.commands.CreateRemodelerCommand;


public interface RemodelerCommandService {
    Long handle(CreateRemodelerCommand command);
}
