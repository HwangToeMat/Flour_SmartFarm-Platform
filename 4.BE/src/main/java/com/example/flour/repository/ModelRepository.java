package com.example.flour.repository;

import com.example.flour.model.entity.Model;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.stereotype.Repository;

@Repository
@NoRepositoryBean
public interface ModelRepository extends JpaRepository<Model, Long> {
}
