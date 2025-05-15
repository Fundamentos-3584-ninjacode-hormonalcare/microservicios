package com.innovasoft.remodify.platform.information.profiles.domain.model.queries;

public record GetContractorByIdQuery(Long ItemId) {

    public GetContractorByIdQuery {
        if (ItemId == null) {
            throw new IllegalArgumentException("id cannot be null");
        }
    }

    public Long getId() {
        return ItemId;
    }
}
