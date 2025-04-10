package com.example.fullStackDemo;

import jakarta.persistence.*;

// import jakarta.persistence.Id;
// import jakarta.persistence.Entity;

@Entity
public class Customer

    {
        @Id // PRIMARY KEY (unique number!)
        @GeneratedValue(strategy = GenerationType.IDENTITY) // auto-indexed ID # (PK)
        private Long id;

        private String name;
        private String address;

        public Customer(Long id, String name, String address) {
            this.id = id;
            this.name = name;
            this.address = address;
        }

        public Customer() {
        }

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getAddress() {
            return address;
        }

        public void setAddress(String address) {
            this.address = address;
        }

        @Override
        public String toString() {
            return "Customer{" +
                    "id=" + id +
                    ", name='" + name + '\'' +
                    ", address='" + address + '\'' +
                    '}';
        }
    }

