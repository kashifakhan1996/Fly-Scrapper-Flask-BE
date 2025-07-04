from flask import Blueprint,jsonify, request
from app.services.skyscanner import fetch_flight_data

flights_bp = Blueprint('flights',__name__)

testData = [
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T02:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T00:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF7445"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T02:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T00:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF7488"
    },
    {
        "Airline": "National Jet Express",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T02:32:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T01:20:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "WO7488"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:05:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5401"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:05:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1801"
    },
    {
        "Airline": "Cathay Pacific",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:05:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "CX9000"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:05:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA3555"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:05:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF401"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5494"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1834"
    },
    {
        "Airline": "Cathay Pacific",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "CX9001"
    },
    {
        "Airline": "American Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "AA7324"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF403"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5405"
    },
    {
        "Airline": "China Southern Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "CZ7557"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1805"
    },
    {
        "Airline": "IndiGo",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "6E4671"
    },
    {
        "Airline": "Cathay Pacific",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "CX9003"
    },
    {
        "Airline": "American Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "AA7389"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:00:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:25:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF405"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:10:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ503"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4122"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6862"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA806"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4124"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6808"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA808"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ505"
    },
    {
        "Airline": "British Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "BA7437"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5409"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1809"
    },
    {
        "Airline": "IndiGo",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "6E4672"
    },
    {
        "Airline": "Cathay Pacific",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "CX9130"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF409"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4126"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6850"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T08:50:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA810"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA812"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF415"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA814"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF417"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA816"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF419"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4118"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6836"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA800"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T07:40:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T06:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ501"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF425"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:25:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:50:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ515"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF427"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA824"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T11:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA826"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T11:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF431"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T11:25:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ509"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T11:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T10:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF433"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T11:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T10:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA830"
    },
    {
        "Airline": "Qatar Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QR7132"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6810"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T14:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T12:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF443"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T14:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T13:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF445"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T15:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T13:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ535"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T15:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T13:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF447"
    },
    {
        "Airline": "British Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "BA7441"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5415"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1815"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4130"
    },
    {
        "Airline": "Qatar Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QR4232"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6848"
    },
    {
        "Airline": "United Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T07:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "UA7444"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T12:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T10:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA832"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T14:15:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T12:40:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ517"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T15:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T14:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF449"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T15:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T14:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA846"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T16:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T14:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF451"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T16:15:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T14:40:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ519"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T16:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T14:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF453"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T16:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T15:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA850"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T16:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T15:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF455"
    },
    {
        "Airline": "LATAM Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "LA4900"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA3561"
    },
    {
        "Airline": "Jetstar",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T09:55:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:15:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "JQ507"
    },
    {
        "Airline": "Hawaiian Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "HA4134"
    },
    {
        "Airline": "Singapore Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "SQ6834"
    },
    {
        "Airline": "Qatar Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QR7192"
    },
    {
        "Airline": "Virgin Australia",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "VA820"
    },
    {
        "Airline": "Bangkok Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "PG4582"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5423"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1823"
    },
    {
        "Airline": "IndiGo",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "6E4677"
    },
    {
        "Airline": "American Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "AA7360"
    },
    {
        "Airline": "British Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "BA7449"
    },
    {
        "Airline": "LATAM Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "LA4812"
    },
    {
        "Airline": "Qantas",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:05:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:30:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "QF423"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5284"
    },
    {
        "Airline": "Bangkok Airways",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "PG4586"
    },
    {
        "Airline": "IndiGo",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "6E4678"
    },
    {
        "Airline": "Air New Zealand",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "NZ1838"
    },
    {
        "Airline": "American Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "AA7366"
    },
    {
        "Airline": "LATAM Airlines",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:20:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T08:45:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "LA4813"
    },
    {
        "Airline": "Emirates",
        "Arrival Airport": "Melbourne - Tullamarine Airport",
        "Arrival Time": "2025-07-03T10:35:00+00:00",
        "Departure Airport": "Sydney Kingsford Smith Airport",
        "Departure Time": "2025-07-03T09:00:00+00:00",
        "Flight Date": "2025-07-03",
        "Flight Number": "EK5427"
    }
]

@flights_bp.route('/flights', methods=['GET'])
def get_flights():
    return testData
    origin = request.args.get('origin', default='IND')
    destination = request.args.get('destination', default='AUS')
    days_to_fetch = int(request.args.get('days', 7))
    data = fetch_flight_data(origin, destination, days_to_fetch)
    return jsonify(data)
