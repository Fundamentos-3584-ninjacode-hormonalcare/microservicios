package com.innovasoft.remodify.platform.iam.domain.model.commands;

public record UpdateUserCommand (Long id,String email, String description, String phone, String image){
}
