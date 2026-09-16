# Luis email draft — Thyroid Report Project discovery

**Status:** DRAFT FOR RICK TO SEND. Gio never contacts Luis directly.

**Subject:** Re: Thyroid Report Project

Luis,

Thank you for sending the thyroid report outline and sample image. I reviewed both. I believe the first version is feasible if it reads the machine-generated measurement table from the cropped image, prefills the thyroid lobe measurements and volumes, and then builds the structured report from your dropdown and free-text selections. You would review and confirm every value before using the report.

Before I define the final scope, I would like to spend a few hours observing your complete thyroid ultrasound workflow. I want to see how the measurements appear across different studies and machines, how you document multiple nodules, and whether you select the TI-RADS category yourself or calculate it from the individual ultrasound characteristics.

I also noticed one item I want to confirm. The outline identifies the highly suspicious category as TI-RADS 4. Should that be TI-RADS 5?

If possible, please have several representative studies available, including a straightforward case, a difficult image, and a case with multiple nodules. We can use de-identified examples while I document the workflow and requirements. With your permission, I would also like to record the screen locally while you walk through the process so I can capture each step accurately without relying on memory.

The thyroid project will be the main focus. I am also working on RadAssist Calcium Score refinements based on your feedback about larger images and cropping. My goal is to have an updated version and a short test script ready tomorrow so we can walk through the changes together, see how they perform in your real workflow, and identify any remaining friction. I would also like to collect the baseline numbers we still need on studies per week, minutes per study, and corrections.

Confirmed with Luis: Wednesday, September 2, at 3:00 PM for a few hours.

Before we test RadAssist, please open it in a fresh private or incognito browser window so the newest build loads instead of an older cached version. If anything looks off, refresh and run it again before we flag it.

Thank you,

Rick

---

## Internal notes — do not send

- Keep thyroid first in the meeting; discuss RadAssist refinements when the flow permits.
- Bring Plaud and use the software-requirements elicitation template.
- Screen recording: prefer local OBS or QuickTime capture saved to encrypted local storage. Do not use Teams/Zoom cloud recording for any screen that may display PHI. Use de-identified studies; obtain Luis's permission before recording.
- Ask for pre/post RadAssist volume, minutes per study, crop retries, and corrected fields.
- Clarify whether the thyroid tool reads measurement tables/annotations or is expected to interpret raw ultrasound anatomy. Do not blur those scopes.
- Confirm whether lobe volume is supplied or calculated, how nodules are added/edited/deleted, and whether recommendations apply per nodule or only to the highest-risk nodule.
- Do not quote price until the workflow and product boundary are confirmed.
