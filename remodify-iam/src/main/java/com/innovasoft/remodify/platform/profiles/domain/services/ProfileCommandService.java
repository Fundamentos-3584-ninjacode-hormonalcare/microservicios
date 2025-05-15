package com.innovasoft.remodify.platform.profiles.domain.services;

import com.innovasoft.remodify.platform.profiles.domain.model.commands.CreateProfileCommand;

public interface ProfileCommandService {
    Long handle(CreateProfileCommand command);
}
