# Active FDO: Governance-Aware Segment Specification for DOIP 2.0

**Abstract**
This repository serves as the reference implementation for the theoretical framework presented in the Springer Nature paper: *"Bridging Global Interoperability and Regional Sovereignty: The Active FDO Protocol Extension."* It addresses the critical "governance gap" in current Digital Object Interface Protocol (DOIP) specifications by introducing a machine-actionable metadata layer at the transport segment level. This enables granular, deterministic compliance enforcement (e.g., GDPR, China Data Security Law) at line speed without deep packet inspection.

---

## 1. DOIP Segments Specification (Original Scope)

Following the DIGITAL OBJECT INTERFACE PROTOCOL SPECIFICATION VERSION 2.0 NOVEMBER 12, 2018
this repository hosts the Json Schema Objects for validating the
segmentes described in the specification.

Please refer to https://www.dona.net/sites/default/files/2018-11/DOIPv2Spec_1.pdf
or use the [PID](http://hdl.handle.net/0.100/DO-IRPV3.0)

The specification includes the following basic operations: hello, create, access, update, delete, search, and
listOperations

### Structure

- The subfolders "doip-request-segments" and "doip-response-segments" contain the request and response segments for the
  DOIP basic operations. Those operations are: Hello, Create, Retrieve, Update, Delete, Search, and ListOperations.
- The subfolder "doip_do_serialization" contains the JSON schema for a serialized DO.
- The subfolders "doip-ex-request-segments" and "doip-ex-response-segments" contain the request and response segments
  for two extended operations: Extended-Create and Extended-Update. Those operations have the same effect as the basic
  Create and Update operations, except that the type-value-pairs that should be written into the PID record by the
  repository are specified in the respective request/response schema.
- Further extended Operations such as Op.CreateFDO can be added following the naming convention.

### Work in Progress

* Other serialization next to json will be created and uploaded.
* The segments might be registered in the [type registry](https://typeregistry.lab.pidconsortium.net) and the Json schemas
  will then be derived from those defintions.

---

## 2. Active FDO Theoretical Foundation

The core innovation is the transformation of passive data segments into "Active Digital Objects" capable of self-description. This allows network nodes to function as Deterministic Finite Automata (DFA), enforcing sovereignty rules based on the tuple:

$$ \Psi(S_{\text{header}}, N_{\text{context}}) \rightarrow \{ \text{FORWARD}, \text{DROP}, \text{INSPECT}, \text{ENCRYPT} \} $$

Where:
*   $S_{header}$ contains the immutable governance metadata (Sensitivity Level, Policy ID).
*   $N_{context}$ represents the node's jurisdictional and security clearance.

---

## 3. Repository Structure (Active FDO Extensions)

*   `fdo_segment_test.py`: The Proof-of-Concept (POC) implementation demonstrating the "Compliance Filter Logic."
*   `DOIP_Active_Segment_Proposal.md`: The formal specification for the 56-byte Active Segment Header.
*   `Policy_Dictionary.json`: A structured mapping schema linking hex codes to real-world legal frameworks.
*   `FDO_Governance_Whitepaper_Draft.md`: High-level architectural summary.

---

## 4. Getting Started with Active FDO

To replicate the "Active Segment Governance" experiment:

### Prerequisites
*   Python 3.8+
*   Standard library modules (`os`, `hashlib`, `struct`, `random`)

### Execution
Run the POC simulation to observe the compliance filter in action:

```bash
python fdo_segment_test.py
```

### Expected Output
The script will:
1.  Generate a dummy 1MB file.
2.  Split it into segments, tagging the first 128KB as **Sensitive (0x02)** and the rest as **Public (0x00)**.
3.  Simulate transmission through an **External Node**.
4.  **Result:** The external node will autonomously identifying and **BLOCK** the sensitive segments while forwarding the public ones, demonstrating granular data sovereignty.

---

## 5. Policy Mapping Schema

The `Policy_Dictionary.json` file serves as the "Rosetta Stone" for the compliance engine, translating abstract legal requirements into machine-readable directives.

| Policy ID | Legal Framework | Description | Action |
| :--- | :--- | :--- | :--- |
| **0x0001** | **China DSL Art. 21** | Core Data (National Security) | **DROP** |
| **0x0002** | **China DSL Art. 21** | Important Data (Restricted) | **INSPECT & LOG** |
| **0x0003** | **Open Science** | General Research Data | **FORWARD** |
| **0x0004** | **PIPL Art. 28** | Sensitive Personal Information | **ENCRYPT OR DROP** |

By editing this JSON file, network administrators can dynamically update the compliance logic of all nodes without modifying the underlying protocol code.

---

## 6. Contact & Citation

**Lead Researcher:** Bin Zhang (GitHub: joy7758)
**Affiliation:** FDO Standards Architecture Group

*For academic citations, please refer to the upcoming Springer Nature publication.*
