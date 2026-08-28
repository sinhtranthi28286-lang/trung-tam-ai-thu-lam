# Trung tâm AI — Audit report

- **PASS — JavaScript syntax**
- **PASS — Duplicate HTML IDs**: {}
- **PASS — Inline handlers defined**
- **WARN — getElementById targets exist**: c-, editPermInline, vdPdfViewer
- **INFO — localStorage keys**: thu_lam_current_username, thu_lam_username
- **INFO — IndexedDB databases**
- **INFO — Supabase tables referenced**: admin_users, ai_areas, ai_tasks, app_files, app_permissions, app_shared_state, app_state_history, app_users, kho-nghiep-vu-so, staff_members, xa_directives
- **WARN — Shared-data persistence**: Công việc/kết luận/báo cáo điều khiển đang lưu localStorage; File văn bản đang lưu IndexedDB cục bộ; Dữ liệu cập nhật nâng lương có dấu hiệu lưu cục bộ
- **INFO — App version**: 8.35
- **INFO — External scripts**: https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js; https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js; https://unpkg.com/docx@8.5.0/build/index.umd.js; https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2
- **INFO — Implicit DOM globals used**: ttStaffRows, ttStaffSearch, wUpdateFile, wUpdateNote, wUpdateOutDate, wUpdateOutNo, wUpdateProgress, wUpdateResult, wUpdateStatus, wUpdateTask