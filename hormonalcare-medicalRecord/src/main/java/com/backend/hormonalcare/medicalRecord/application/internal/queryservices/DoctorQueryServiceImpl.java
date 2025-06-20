package com.backend.hormonalcare.medicalRecord.application.internal.queryservices;

import com.backend.hormonalcare.medicalRecord.domain.model.aggregates.Doctor;
import com.backend.hormonalcare.medicalRecord.domain.model.queries.*;
import com.backend.hormonalcare.medicalRecord.domain.services.DoctorQueryService;
import com.backend.hormonalcare.medicalRecord.infrastructure.persistence.jpa.repositories.DoctorRepository;
import com.backend.hormonalcare.medicalRecord.application.internal.outboundservices.acl.ExternalProfileService;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DoctorQueryServiceImpl implements DoctorQueryService {
    private final DoctorRepository doctorRepository;
    private final ExternalProfileService externalProfileService;

    public DoctorQueryServiceImpl(DoctorRepository doctorRepository, ExternalProfileService externalProfileService) {
        this.doctorRepository = doctorRepository;
        this.externalProfileService = externalProfileService;
    }

    @Override
    public Optional<Doctor> handle(GetDoctorByIdQuery query) {
        Optional<Doctor> doctorOptional = doctorRepository.findById(query.id());
        if (doctorOptional.isEmpty()) {
            return Optional.empty();
        }

        Doctor doctor = doctorOptional.get();
        Optional<ExternalProfileService.ProfileDetails> profileDetailsOptional = externalProfileService.fetchProfileDetails(doctor.getProfileId());

        if (profileDetailsOptional.isEmpty()) {
            return Optional.of(doctor);
        }

        ExternalProfileService.ProfileDetails profileDetails = profileDetailsOptional.get();

        // For now, returning the doctor entity as is.
        return Optional.of(doctor);
    }

    @Override
    public Optional<Doctor> handle(GetDoctorByProfileIdQuery query) {
        return doctorRepository.findByProfileId(query.profileId());
    }

    @Override
    public Optional<Doctor> handle(GetDoctorByDoctorRecordIdQuery query) {
        return doctorRepository.findByDoctorRecordId(query.doctorRecordId());
    }

    @Override
    public Optional<Long> handle(GetProfileIdByDoctorIdQuery query) {
        return doctorRepository.findById(query.doctorId())
                .map(Doctor::getProfileId) ;
    }

    @Override
    public List<Doctor> handle(GetAllDoctorsQuery query) {
        var doctors = doctorRepository.findAll();
        doctors.forEach(doctor -> {
            var profileDetailsOptional = externalProfileService.fetchProfileDetails(doctor.getProfileId());
            profileDetailsOptional.ifPresent(profileDetails -> {
            });
        });
        return doctors;
    }

}
