package com.example.fullStackDemo;

import org.springframework.data.jpa.repository.*;

import java.util.List;


public interface CustomerRepository extends JpaRepository<Customer, Long>
    {   // empty or with method declarations like below
        // inherits CRUD methods: save, delete, count, & find
        public List<Customer> findByName(String Name);

    }