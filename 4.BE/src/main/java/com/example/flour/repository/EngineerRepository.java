package com.example.flour.repository;

import com.example.flour.model.entity.Engineer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.stereotype.Repository;

@Repository
@NoRepositoryBean
public interface EngineerRepository extends JpaRepository<Engineer, Long> {
}
