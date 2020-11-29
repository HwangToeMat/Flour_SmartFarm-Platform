package com.example.flour.repository;

import com.example.flour.model.entity.ModelDetail;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;
import org.springframework.stereotype.Repository;

@Repository
@NoRepositoryBean
public interface ModelDetailRepository extends JpaRepository<ModelDetail, Long> {

}
