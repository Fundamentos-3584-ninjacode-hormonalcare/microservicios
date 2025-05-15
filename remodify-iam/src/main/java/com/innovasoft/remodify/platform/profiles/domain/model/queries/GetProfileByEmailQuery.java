package com.innovasoft.remodify.platform.profiles.domain.model.queries;

import com.innovasoft.remodify.platform.profiles.domain.model.valueobjects.EmailAddress;

public record GetProfileByEmailQuery(EmailAddress emailAddress) {
}