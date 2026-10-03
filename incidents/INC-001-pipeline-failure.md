# INC-001 — Sales Pipeline Failure

## Incident Type
Data Pipeline Failure

## Pipeline
SalesDataPipeline

## Severity
Medium

## Issue

The transformation pipeline failed during data validation.

## Detection

The pipeline monitoring process detected a failed pipeline run.

## Investigation

The source data contained an invalid amount value.

The affected record contained a negative transaction amount.

## Root Cause

Invalid source data passed into the transformation stage.

## Resolution

Added validation rules to identify:

- Missing customer IDs
- Invalid transaction dates
- Negative transaction amounts
- Duplicate transaction IDs

Invalid records were excluded from the processed dataset.

## Preventive Action

- Add data validation before transformation
- Monitor pipeline failures
- Track recurring data-quality issues
- Document incidents
- Add automated alerts for future failures

## Status

Resolved