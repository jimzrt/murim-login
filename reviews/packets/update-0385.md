<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0385.txt",
      "sha256": "217b2c833411a34181d7cf7d6068f8c3e37be5a3a0964233cab5516014cdb89d",
      "bytes": 16200
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "68e2a293f074ee484bf801d81cb16a4cb79d8117d0dd80c7263c206ea4399f36",
      "bytes": 4670
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f658da8b34ae58b2b95ab34b50f266d82ebc339ff925a6407f04099dcfa63980",
      "bytes": 11627
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4dabb752047f7999c181e8ca859069c06dbd31848b644502901cefd2f083ff75",
      "bytes": 23777
    },
    {
      "path": "characters/Wei Penghu.md",
      "sha256": "c5618d8a155c80d4ccbfe882890b4eab1183e5116ea35f48f9f536b75a5fe11c",
      "bytes": 607
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "098ab312e526a807e76c2efd4e97c16e08859d6ef207eea932a3a0c7ef5a4e5a",
      "bytes": 6810
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 15683
}
-->

# Durable State Update — Chapter 385

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 385. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 385. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 385,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 385,
    "continuity_sources": [385],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is a Supreme Peak martial artist; his exact current level, Fame, complete Titles, martial-art stages, and unassigned points remain unstated.",
    "Taekyung has returned to the modern world and is working with Chinese authorities to stop the monster disaster while seeking Lei Fei and the missing Sichuan Hunters.",
    "Sichuan Province remains in a wartime state, and the current monster wave began in Gaoping District, Nanchong City, after a sudden mana surge.",
    "Wei Penghu is a Senior General and Minister of Defense at the Central Military Commission, and he raised his missing nephew Lei Fei as his own son.",
    "Wei Penghu's jet has reached the temporary operations headquarters in a deep bunker beneath Mount Qingcheng.",
    "Xiao Yang is Chairman of the Central Military Commission of the Chinese Communist Party, General Secretary, and state chairman of the People's Republic of China.",
    "Xiao Yang has asked the assembled Hunters to prioritize human lives and stop the disaster, while taking personal responsibility and retaining full authority.",
    "Team Leader Choi accompanies Taekyung and continues to trust him during the Chinese crisis.",
    "Magic Johnson is an S-rank Hunter, one of three Archmages worldwide, and a combat-specialized War Mage.",
    "Magic Johnson recognizes Taekyung's Sibeol-jwa nickname, which is known even to his youngest daughter.",
    "At least four additional S-rank Hunters are gathered in the bunker: one Chinese man, one Chinese woman, and two Western men.",
    "An unnamed young Chinese Hunter has insulted Taekyung with the slur peninsula bangzi, and Taekyung has answered with an offensive insult toward mainland Chinese people.",
    "The Chengdu International Airport attack involved an undead army controlled by three incomplete Arch Liches, all of whom Taekyung destroyed.",
    "The Skeleton Warlord absorbed the death energy of the remaining two Arch Liches and became much stronger, but the persistence and full extent of that increase remain unknown.",
    "Dark Heaven's agents, purpose, and connection to the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan was devastated by Dark Heaven, owes Taekyung's group a debt, and is considering relocation.",
    "Mungyeong remains torn between Dongbong's warning about an approaching war and his stated wish to leave Murim affairs behind.",
    "Ae-hyang appears to serve an unidentified superior after a sinister red light entered her eyes, and the Sichuan Governor's false memorial remains unresolved.",
    "Lei Fei's fate and the fate of the Public Security Armed Forces Hunters who disappeared with him remain unresolved."
  ],
  "continuity_sources": [
    384
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved.",
    "Dark Heaven's larger purpose, its reason for sparing Taekyung, and the origin and function of the hidden transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination, along with the timing and outcome of the Samgoe escort to Henan, remain unresolved.",
    "The request Dongbong wants to make of Taekyung, Mungyeong's eventual response to the coming war, and the identity and fate of the boy from the Chengdu port remain unresolved.",
    "Ae-hyang's superior and the consequences of the Sichuan Governor's false memorial remain unresolved.",
    "The relationship between the Lich and the Arch Lich, the full extent of the Skeleton Warlord's increased power, and the monster wave's larger plan remain unresolved.",
    "Lei Fei's fate and the fate of the missing Sichuan Hunters remain unresolved.",
    "The identities and roles of the other international S-rank Hunters gathered at Mount Qingcheng remain unresolved."
  ],
  "safe_through": 384,
  "temporary_decisions": [
    "Use the current Korean source as authoritative; the skipped range is not accepted English continuity.",
    "Render Zhonghua as Zhonghua and preserve the Jongseok mishearing joke for 총서기.",
    "Render Xiao Yang's offices as Chairman of the Central Military Commission, General Secretary, and state chairman.",
    "Render 대마법사 as Archmage and 워 메이지 as War Mage.",
    "Retain Teacher Jin for 진 선생 and Comrade Chairman for 주석 동지.",
    "Render 반도의 빵즈 as peninsula bangzi and retain the derogatory-slur footnote.",
    "Preserve Taekyung's conversational, self-mocking first-person voice and the source's offensive insult exchange.",
    "Render 수치사 as death by humiliation in Taekyung's internal joke."
  ],
  "version": 1
}
```

## Expedition bridge dossier

# Expedition Seed Dossier

This dossier is intentionally conservative. It orients the Chapter 370 catch-up.
It is not a substitute for translating Chapters 66–369, and it must not leak
plot from parked Chapters 371–375.

## Hard boundary

- Accepted English continuity is reliable through Chapter 65.
- Chapters 66–369 are skipped and have no accepted local English in this
  expedition.
- Chapter 370 is the next chapter to translate. Its Korean source is the
  authority for every beat in that chapter.
- Parked accepted translations of Chapters 374–375 exist in this branch. Do not
  read them, their reviews, or old 371–373 bridge summaries while drafting
  370–373.
- When the Korean source of the current chapter conflicts with this dossier or
  with Chapter 65 continuity, the current source wins. Do not invent missing
  backstory; preserve ambiguity and flag an unresolved continuity issue.

## Opening position for Chapter 370

Chapter 370's source opens at the Sichuan Tang Clan. About seven days have
passed since the Three-Sect Bloodbath. The clan's gates, long closed, are open
to reconstruction and to orthodox guests. Do not assert later names, ranks,
quests, or outcomes that the current chapter has not yet shown.

## Translation guardrails

- Treat the Korean source as authoritative for every line of the chapter being
  translated.
- Do not back-project titles, names, ranks, or skills from parked later
  chapters or web searches into the skipped range without current-source
  evidence.
- Use established local terminology where it exists from Chapters 0–65.
- For terms first evidenced in the current source, follow the ledger and
  first-use rules. Record new bindings through the normal update stage.
- The light, self-mocking first-person voice and the source's jokes remain
  important, but missing continuity must never be filled by invented exposition.

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 독룡각 | **Poison Dragon Pavilion** | Pavilion led by Tang Horyong |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 오대세가 | **Five Great Families** | Major orthodox families |
| 소림혈사 | **Shaolin Bloodbath** | Earlier attack that galvanized orthodox Murim |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 사죄와 용서 | **Atonement and Forgiveness** | Hidden Quest completed by Taekyung. |
| 당문의 은인 | **Benefactor of the Tang Clan** | Title acquired by Taekyung. |
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 묘령사태 | **Satae Myo Ryeong** | Middle-aged Emei nun overseeing the funeral prayers. |
| 명진 | **Myeongjin** | Daoist assisting with the funeral rites. |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 후개 | **Future Beggar Chief** | Title used for Gung Gibang. |
| 기련삼괴 | **Qilian Samgoe** | The trio of monsters that includes Samgoe and Ilgoe. |
| 일괴 | **Ilgoe** | The strongest of the Qilian Samgoe, defeated single-handedly by Jin Taekyung. |
| 칠선자 | **Chilseonja** | Mysterious martial artist who blocked Samgoe's attack and saved Hyuk Mujin. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |
| 천주 | **Heavenly Lord** | Being worshiped as a god by Dark Heaven's fanatics. |
| 혈주 | **Blood Lord** | Dark Heaven figure whose power and abilities are recalled by Jin Taekyung. |
| 열화동 | **Blazing Fire Cave** | Cave at Mount Jiuhua containing an advanced arcane formation. |
| 진성애 | **Jin Seong-ae** | Jin Taekyung's joking title for himself as a sex-education teacher. |
| 구성애 | **Gu Seong-ae** | Real-world sex-education teacher referenced in Jin Taekyung's joke. |
| 삼도천 계곡 | **Valley of the Sanzu River** | Valley named after the Buddhist river separating the living world from the afterlife. |
| 노군백 | **No Gunbaek** | Level 170 opponent named in a System defeat message. |
| 귀염미 | **Gwiyeommi** | Pen name of a romance novelist. |
| 홍무 | **Hongwu** | Era name beginning when the civil war ends and a new emperor ascends. |
| 성도 | **Chengdu** | City whose western port is the departure point. |
| 선화아 | **boatman** | Nautical title used for Mu Song. |
| 무송 | **Mu Song** | Bronze-skinned boatman associated with the water bandits. |
| 애향 | **Ae-hyang** | The Sichuan Governor's favorite concubine; covertly manipulative. |
| 상산왕 | **King of Shangshan** | Noble whose token was carried by Taekyung's group. |
| 수룡채 | **Water Dragon Stronghold** | Stronghold whose flag flies from the ships carrying Taekyung's group. |
| 흑룡갑 | **Black Dragon Armor** | The armor's former name; only a fragment survives. |
| 화룡갑 | **Flame Dragon Armor** | New name Taekyung gives the bound armor fragment. |
| 열화신공 | **Blazing Flame Divine Art** | Art whose formula Taekyung uses to infuse the armor. |
| 삼공 | **Grand Councilor** | High office referenced in the Sichuan Governor's ambitions. |
| 최 팀장 | **Team Leader Choi** | Taekyung's modern-world team leader aboard the private jet. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 스켈레톤 워로드 | **Skeleton Warlord** | Undead commander accompanying Taekyung's group. |
| 샤오 양 | **Xiao Yang** | Chairman credited by passengers with making a special request for Taekyung. |
| 중국 중앙위원회 | **Central Committee of China** | Organization that sent the private jet. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 청두 국제공항 | **Chengdu International Airport** | Destination airport under attack. |
| 헌터 마켓 | **Hunter Market** | Market where Taekyung bought the spear at a discount. |
| 검은 별 | **Black Star** | Epithet of the exceptionally powerful lead wyvern. |
| 샤오 쉔 | **Shao Shen** | Twenty-year-old spear-wielding Hunter of the Public Security Armed Forces. |
| 야오위 | **Yao Wei** | A-rank Hunter, Shao Shen's friend and comrade. |
| 류인친 | **Ryu Inchin** | Named combatant of the Public Security Armed Forces; exact relationship to the person calling him hyung is unresolved. |
| 공안 무력부 | **Public Security Armed Forces** | Chinese Hunter organization. |
| 인민 해방군 | **People's Liberation Army** | Chinese military force stationed at the airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 오성홍기 | **Five-Star Red Flag** | National flag of the People's Republic of China. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 중앙 군사 위원회 | **Central Military Commission** | Chinese military body Shao Shen assumes dispatched the unknown S-rank Hunter. |
| 화염신장 | **Flame Divine Palm** | Named fire-based palm technique used by Taekyung. |
| 멸염신권 | **Flame-Annihilating Divine Fist** | Named fire-based fist technique used by Taekyung. |
| 염화일로 | **Flamefire Path** | Named fire-based movement technique used by Jin Taekyung. |
| 아크 리치 | **Arch Lich** | Superior undead being referenced by the three incomplete Liches. |
| 스켈레톤 메이지 | **Skeleton Mage** | Undead unit the three beings consider deploying. |
| 데스나이트 | **Death Knight** | Powerful undead being the three beings plan but fail to create. |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 언데드 헌터 | **Undead Hunter** | Title acquired by Jin Taekyung as the Unexpected Assault Quest Reward. |
| 죽음의 강 | **River of Death** | River upon which the undead swear binding oaths. |
| 검은 숲 | **Black Forest** | Domain the Skeleton Warlord claims to rule. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 상장 | **Senior General** | Wei Penghu's military rank, explained as four-star. |
| 오르페우스 폰 막시무스 발렌시아 바이엘른 | **Orpheus von Maximus Valencia Bayern** | Self-styled name used by one of the three undead beings; retains the source's humorous wordplay. |
| 레이페이 | **Lei Fei** | Previously undisclosed Chinese S-rank Hunter and commander of the Sichuan Public Security Armed Forces; missing with his Hunters. |
| 난충시 | **Nanchong City** | City containing Gaoping District, where the monster wave began. |
| 가오핑구 | **Gaoping District** | District in Nanchong City where the first monster-wave signs appeared. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |
| 핑핑이 | **Pingping** | Taekyung's joking guess at the name of the deceased former chairman; not established as the actual name. |
| 팽팽이 | **Pengpeng** | Taekyung's joking alternative guess at the name of the deceased former chairman; not established as the actual name. |
| 매직 존슨 | **Magic Johnson** | S-rank Hunter, one of the three Archmages, and a combat-specialized War Mage. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |
| 워 메이지 | **War Mage** | Magic Johnson's combat-specialized Archmage title. |
| 총서기 | **General Secretary** | One of Xiao Yang's offices. |
| 국가 주석 | **state chairman** | Xiao Yang's office as leader of the People's Republic of China. |
| 중앙군사위원회 | **Central Military Commission** | Commission chaired by Xiao Yang. |
| 중국 공산당 | **Chinese Communist Party** | Party whose Central Military Commission Xiao Yang chairs. |
| 종석이 | **Jongseok** | Taekyung's mistaken personal-name joke for the General Secretary; not the chairman's actual name. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 청풍고검 | junior_to_elder_sect_leader | Perfected One | respectful-formal | Uses 진인 when greeting the Qingcheng Sect Leader. |
| 청풍고검 | 진태경 | elder_sect_leader_to_junior_ally | Fellow Daoist Jin | respectful-but-familiar | Uses 진 도우 when greeting Taekyung. |
| 멸절신니 | 진태경 | elder_sect_leader_to_benefactor | Benefactor Jin | respectful-formal | Uses 진 시주 when greeting Taekyung. |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |
| 진태경 | 문경 | ally_to_secret_identity_holder | Mungyeong | casual-but-teasing | Taekyung accepts the requested name and deliberately uses it in a familiar vocative. |
| 동봉 | 문경 | disciple_to_master | Master | deferential | Dongbong repeatedly addresses Mungyeong as 스승님 after affirming his identity as the Divine Physician. |
| 무송 | 진태경 | older_ally_to_junior_ally | junior | deferential-but-uncertain | Mu Song switches from junior to Young Hero Jin and Great Hero before Taekyung tells him to use junior. |
| 사천성주 | 애향 | lover_to_favorite_concubine | Ae-hyang | intimate-affectionate | The Sichuan Governor repeatedly calls his favorite concubine by name and speaks to her in an indulgent intimate manner. |
| 애향 | 사천성주 | favorite_concubine_to_lover | my dear | intimate-coquettish | Ae-hyang addresses the Sichuan Governor as 가가 while flattering and manipulating him. |
| 진태경 | 최 팀장 | subordinate_to_team_leader | Team Leader | polite-but-direct | Taekyung uses 팀장님 while asking Choi for help and addressing him during the crisis. |
| 최 팀장 | 진태경 | team_leader_to_trusted_hunter | Mr. Jin Taekyung | professional-deferential | Choi repeatedly uses 진태경 씨 while relying on Taekyung to resolve the attack. |
| 진태경 | 기장 | passenger_to_captain | Captain | casual-urgent | Taekyung directly asks the captain for permission before cutting open the aircraft door. |
| 샤오 쉔 | 진태경 | foreign_hunter_to_recognized_hero | Teacher Jin | formal-polite | Uses 진 선생님 after recognizing Taekyung as Sibeol-jwa. |
| 스켈레톤 워로드 | 진태경 | undead_subordinate_to_human_controller | vile human | hostile-but-familiar | Recurring address used while speaking to Taekyung during the battle. |
| 진태경 | 스켈레톤 워로드 | human_controller_to_undead_subordinate | Boney | casual-teasing | Taekyung uses Boney as a deliberately demeaning pet nickname. |
| 웨이펑후 | 진태경 | senior_military_official_to_foreign_hero | Teacher Jin | respectful-formal | Wei Penghu uses 진 선생 when introducing himself and inviting Taekyung to the operations headquarters. |
| 조종사 | 웨이펑후 | pilot_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Pilot's formal greeting on Wei Penghu's arrival. |
| 웨이펑후 | 샤오 쉔 | senior_military_official_to_subordinate_hunter | Senior Colonel Shao Shen | respectful-but-familiar | Wei Penghu uses Shao Shen's rank and name when bidding him farewell. |
| 샤오 쉔 | 웨이펑후 | subordinate_hunter_to_senior_military_official | Comrade Minister of Defense | deferential-formal | Shao Shen promises to complete his mission and rejoin Wei Penghu. |
| 샤오 양 | 진태경 | head_of_state_to_foreign_hunter | Teacher Jin | respectful-formal | Xiao Yang uses 진 선생 when greeting and addressing Taekyung. |
| 샤오 양 | 웨이펑후 | head_of_state_to_old_friend_and_subordinate | Minister of Defense Wei Penghu | authoritative-but-familiar | Xiao Yang addresses Wei by office and name while discussing authority over the Central Military Commission. |
| 웨이펑후 | 샤오 양 | subordinate_to_head_of_state | Comrade Chairman | deferential-formal | Wei uses 주석 동지 when responding to Xiao Yang. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 대마법사 | **Archmage** | Title held by only three people worldwide. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 384
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Wei Penghu.md

# Wei Penghu (웨이펑후)

- **Safe through:** Chapter 384
- **Aliases:** None
- **Role:** Senior General and Minister of Defense at the Central Military Commission
- **Personality:** Courteous, composed, and direct in his first meeting with Jin Taekyung
- **Voice:** Formal and respectful
- **Relationships:** Meets Jin Taekyung after the Chengdu International Airport battle, brings him toward the temporary operations headquarters, and is Lei Fei's uncle; he raised Lei Fei as his own son and asks Taekyung to bring him back if found.

## Korean source

```text
＃385화



「안 그래, 반도의 빵즈?」

“뭐래, 대륙 짱개 새끼가.”

그 순간, 무거운 적막이 내려앉았다.

매직 존슨과 같은 외국인들은 통역 마법을 사용하면서도 빵즈와 짱깨가 정확히 무슨 의미인지 알아듣지 못해 어리둥절했고, 최 팀장은 작게 혀를 찼으며 한 사람의 얼굴은 돌처럼 딱딱하게 굳었다.

「뭐?」

“뭐, 인마.”

「다시 한번 지껄여 봐라, 빵즈.」

“응. 짱깨.”

「이런 개…….」

“좋아. 정리하자. 나는 개. 너는 짱깨.”

「……!」

놈의 얼굴이 와락 일그러지는 것이 보인다. 자리를 박차고 벌떡 일어나려는 놈을, 옆자리에 앉아 있던 여인이 손을 들어 제지했다.

「그만.」

청량음료처럼 깨끗한 분위기를 지닌 20대 초반의 미녀. 그녀의 입술 사이로 침착한 목소리가 이어졌다.

「부탁이니 적당히 해 줬으면 좋겠는데. 두 사람 모두.」

적당히라…….

잠시 여자를 바라보던 나는 어깨를 으쓱해 보였다.

“뭐, 원하신다면.”

뜻밖의 대답이었는지 그녀의 눈썹이 살짝 휘었다.

「언뜻 듣기로는 만만치 않은 성격이라던데, 생각보다 순순하게 받아들이네?」

“받아들여야죠. 다른 사람도 아니고 당신 부탁인데.”

「미인계에 걸려들었구나? 아, 이래서 예쁘면 피곤하다니까.」

능청스럽게 긴 머리를 쓸어올리는 그녀를 보자 피식 웃음이 나왔다.

“너, 지금 웃었니?”

「생각했던 것보다 재미있는 분 같네요. 파이 첸 씨는.」

파이 첸. 그녀의 이름이다.

대학교 표지 모델 같은 저 용모와 분위기에 속으면 안 된다. 결혼만 하지 않았을 뿐, 쉰 살을 훌쩍 넘긴 장년의 나이니까.

동시에 내게는 까마득한 대선배이자, 대격변의 영웅 중 한 사람이기도 했다.

「처음부터 알고 있었다 이거지. 흠, 요즘 애들은 나 모를 줄 알았는데.」

틀린 말은 아니다. 확실히 파이 첸은 다른 S급 헌터들에 비해 미디어에 노출되는 빈도가 매우 낮았다.

수면 아래에서는 신분을 세탁한 뒤 새로운 삶을 살고 있다는 소식도 심심찮게 들려올 정도였다.

하지만 나는 아주 어릴 때부터 그녀를 알고 있었다.

“저희 어머니가 오랜 팬이시거든요. 그 왜, 이십 년 전쯤에 개봉했던 로맨스 영화에 주연으로 나오셨었잖아요.”

「어머? 그게 도대체 언제 적 이야기니. 그래도 그걸 기억해 주는 사람을 만나니까 반갑네.」

“혹시 나중에 사인받으러 가도 됩니까? 어머니께 파이 첸 씨 사인 가져다드리면 좋아하실 것 같아서요.”

「물론이지. 그리고 앞으로는 그냥 첸 씨라고 해. 풀 네임은 너무 딱딱해 보이잖아. 더 편하게 누님이라고 불러도 되고.」

“예? 무슨 소리세요. 인터넷 검색해 보니까 첸 씨가 저희 어머니보다 다섯 살 많으시던데.”

「……만만치 않네. 듣던 대로.」

하지만 정말 만만치 않은 놈은 따로 있었다.

「이런 자라 좆 같은……!」

끓어오르는 목소리. 우리의 대화로 잠시 잊혔던 놈이 분노에 가득 찬 눈으로 나를 노려보았다.

「이 약소국 빵즈 놈이 감히 누구를 무시하는 거냐. 내가 어떤 사람인 줄 알고!」

“……와, 대사 존나 구려.”

우리를 번갈아 보던 파이 첸이 흥미로운 눈빛으로 턱을 괴었다.

「그러게. 아까부터 궁금했는데 너, 이 애가 누군지는 알고 이러는 거니?」

내 대답을 듣고 싶어 하는 사람은 파이 첸 뿐만 아니었다.

이제 반쯤 해탈한 표정의 최 팀장을 제외한 모두가 내 입만을 바라보고 있었다.

말싸움에서 진 일곱 살 어린애처럼 씨근덕거리는 놈과 미국의 대마법사 매직 존슨. 그리고 영국에서 온 청년까지. 그들을 따라온 수행원들도 예외는 아니었다.

모두의 시선 속에, 나는 고개를 끄덕였다.

「알긴 알죠. 우헤이싱.」

잦은 미디어 노출로는 S급 헌터 중에서도 1, 2위를 다투는 놈이니 모를 수가 없다.

내 대답에 아까부터 빵즈 운운하며 시비를 걸어온 놈, 우헤이싱이 눈을 부릅떴다.

「내가 누구인지 알면서도 그랬단 말이냐?」

“지나가던 개도 알걸? S급 헌터 중에 웬 인간 말종 새끼가 하나 있다는 것 정도는.”

「뭐, 뭐라고?」

“왜? 네 취미가 관심받기. 특기가 범죄 저지른 다음 언론 플레이 하기인 거 모르는 사람이 어디 있다고.”

「……!」

“그러고 보니까 너 이 새끼, 작년쯤에 사고 치지 않았냐? 나라가 내게 허락한 유일한 마약. 뭐 이 지랄 떨면서 공식 SNS에 레이드 한 사진 올리고 한 달 후에 진짜 마약 한 거 걸렸었잖아. 아마 대마초였나?”

“진태경 씨.”

“최 팀장님, 말리지 마세요.”

“대마초가 아닙니다.”

“예?”

불쑥 끼어든 최 팀장이 침착한 목소리로 태경 위키를 수정해 주었다.

“대마초가 아니라 코카인과 필로폰입니다.”

“아, 그랬구나. 알려 주셔서 감사합니다.”

“뭘요. 기왕 이렇게 된 거, 못 할 말이 뭐가 있겠습니까.”

해탈한 표정 보소.

이제는 모든 것을 내려놓고 우화등선(羽化登仙)을 준비 중인 최 팀장을 뒤로한 나는, 우헤이싱을 향해 활짝 웃으며 말을 이었다.

“크으, 어떻게 그런 복선을 깔 생각을 했냐. 이 새끼 최소 우헤이순원. 보랏빛 레이드.”

「뭐, 뭐라고?」

“생각해 보니까 또 있네. 5년 전에 버닝문인가 뭔가 하는 클럽에서 약 타서 성폭행 저지르다가 걸렸던 거. 그거 어떻게 무죄 받았냐? 중국 법으로 이 정도면 두세 번쯤 사형당했어도 이상하지 않은데.”

「……!」

“공산당 최고위층 아들이라는 소문은 들었는데. 돈이랑 권력으로 빠져나온 거야? 이 똑똑한 새끼 보게 이거.”

「주, 주둥이 닥치지 못해! 이 천민 출신 빵즈가 감히!」

얼굴이 시뻘겋게 달아오른 채 고함을 내지르는 우헤이싱의 모습에, 가만히 이 사태를 지켜보던 한 사람이 입을 열었다.

「시끄럽군.」

오만한 목소리가 물 흐르듯 이어졌다.

「경박스럽고 천박해. 듣자 하니 중국 귀족 집안의 핏줄 같은데, 가문의 어른들에게 예법 교육을 받지 못했나?」

목소리의 주인을 확인한 우헤이싱이 입술을 깨물었다.

「다, 당신은…….」

「당신?」

잘 정돈된 갈색 머리카락 아래, 은은한 초록빛 눈동자가 우헤이싱을 천천히 훑더니 떨어진다.

「윌리엄.」

청년의 부름에 뒤에 서 있던 반백의 장년인이 앞으로 나섰다.

먼지 한 톨 묻어 있지 않은 구두와 칼처럼 예리하게 다려진 정장. 우뚝 선 채 좌중을 둘러본 장년인의 입술 사이로 듣기 좋은 중저음이 흘러나왔다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께 모두 일어나 예를 갖추십시오.」

케임브리지 공작이자 스트래선의 백…… 시벌, 뭔 칭호가 저렇게 길어.

어쨌건 필릭스 뭐시기 왕자가 준엄하게 한마디를 덧붙였다.

「다들 편하게 필릭스 왕자 전하라고 부르게.」

“…….”

“…….”

사람들 표정 좀 봐라. 세상에서 제일 불편해 보인다.

물론 그중에서도 가장 압권인 사람은 앞서 내게 천민 운운했던 우헤이싱이었다.

그도 그럴 게, 막상 신분으로 따지면 영국 왕족을 어떻게 이기겠나.

「그, 그러니까 이게…….」

「아하.」

당황하는 우헤이싱을 바라보던 필릭스 왕자가 이제 알았다는 듯 고개를 끄덕였다.

「그렇군. 말 더듬이인가?」

「마, 말더듬이?」

「아니라면 왜 말을 제대로 하지 못하는 거지? 가문에서 스피치 훈련을 받지 못했나?」

왕자 전하 만세.

굳이 직접 나설 필요도 없었다. 영국 왕위 계승 서열 3위가 주사기로 꽂아 주는 탄산에 십이지장까지 톡톡 튀는 기분이다.

입이 찢어질 듯이 웃고 있던 그때, 필릭스 왕자의 시선이 문득 나를 향했다.

「자네.」

“응? 나 말하는 겁니까?”

내 반문에 필릭스 왕자의 뒤에 서 있던 장년인이 입을 열었다.

「케임브리지 공작, 스트래선 백작, 캐릭퍼거스 남작, 가터 훈장의 기사, 시슬 훈장의 기사이신 왕자 필릭스 알렉산더 루이 전하께서 하문하실 때에는…….」

「그만하게. 윌리엄.」

손을 들어 앵무새의 입을 틀어막은 필릭스 왕자가 자애로운 눈빛으로 나를 응시했다.

「본인이 품위를 버리고 이렇게 직접 나선 것은, 평소 신분 격차를 타파해야 한다는 신념을 갖고 있기 때문이라네.」

“……?”

「천민이면 어떻고, 귀족이면 어떤가. 우리는 그저 신 아래 평등한 사람일 뿐인 것을. 그러니 저자의 말에 너무 상처받지 말게.」

아니, 이게 뭔 개소리야.

순간 할 말을 잃은 내게 최 팀장이 넌지시 속삭였다.

“진태경 씨를 천민이라고 생각하는 것 같습니다.”

“……!”

저 왕자 새끼가 미쳤나.

어이없는 표정으로 필릭스 왕자를 바라보는 내게, 천천히 자리에서 일어난 그가 당연하다는 듯한 얼굴로 손등을 내밀었다.

「자, 어서.」

“……어서라니. 이번에는 또 뭔데.”

비서인지 앵무새인지 모를 장년인이 흐뭇한 미소를 띤 채 입을 열었다.

「손등에 입을 맞춰, 필릭스 알렉산더 루이 전하께서 보여 주신 자애로움에 감사를 표하시면 됩니다.」

“…….”

이거 완전 또라이들 아냐.

‘단체로 타입 캡슐 타고 18세기에서 건너왔나, 이 18새기들이.’

잠시 머리가 띵해진 내 귓가에, 최 팀장이 보낸 메시지 마법이 닿았다.

- 안 됩니다.

나는 전음으로 응답했다.

- 뭐가 안 돼요.

- 어쨌든 안 됩니다. 그냥 웃으면서 넘어가십시오. 필릭스 왕자는 원래 좀 별종으로 유명하잖습니까.

- 지금 쟤 손등 부러트리면 더 유명해지지 않을까?

- 안 됩니다. 절대 안 됩니다!

- 손등 조금. 아니면 손가락 하나만이라도.

- 안 된다고!

메시지 마법에 이 정도의 감정이 담길 수 있다니. 최 팀장도 나름대로 절박한 모양이다.

그래, 영국 왕자니까 어쩔 수 없지. 내가 내심 화를 삭이던 그때였다.

「헤이, 시벌좌.」

이건 또 뭐야. 나는 불쑥 다가온 매직 존슨을 경계 어린 눈빛으로 바라봤다.

혐한, 각종 트러블로 유명한 우헤이싱은 애초에 기대부터 안 했지만, TV에서나 보던 S급 헌터들을 실물로 봤다는 기쁨은 서서히 바닥을 드러내고 있었다.

“……아니 제발. 시벌좌 말고 이름으로 부르세요. 제가 존슨을 좆슨이라고 부르면 좋겠어요?”

「음, 듣고 보니 그렇군. 그럼, 진(Jin)?」

“훨씬 낫네요. 그런데 왜요?”

「별건 아니고. 혹시 왕자의 손등에 키스할 생각이 없는 거야?」

충분히 별거 같은데.

어이가 없어진 나는 즉각 되물었다.

“당연하죠. 무슨 중세시대도 아니고. 존슨 같으면 하고 싶겠습니까?”

「난 하고 싶지.」

“예?”

순간 뇌리를 스치는 섬광 같은 깨달음.

깜빡 잊고 있었다. 매직 존슨은 미국의 국민 영웅이자 국민 게이라는 사실을.

타임지가 선정한 ‘세계에서 가장 영향력 있는 성소수자 1위’가 나를 향해 진지한 얼굴로 제안한다.

「그래서 말인데, 내가 진을 대신해서 왕자에게 감사를 표하고 싶어.」

“…….”

이걸 이렇게 포장해 버리네. 하지만 매직 존슨과는 달리 필릭스 왕자는 슬그머니 손등을 회수했다.

「신 아래 우리는 평등한 한 사람의 인간일 뿐. 이런 구닥다리 예법은 없어져야 해. 매직 존슨, 그대의 호의는 나중에 받기로 하지.」

“…….”

저게 조금 전까지만 해도 나한테 손등 내밀던 새끼가 할 말인가? 듣고 있던 파이 첸도 어처구니가 없는지 중얼거렸다.

「어머, 되게 뻔뻔하다. 범죄만 안 저질렀지, 우헤이싱 저 녀석보다 한 수 위일지도 몰라.」

“아무리 그래도 우헤이싱보다는 낫죠. 쟤는 법대로면 사형당했어야 할 놈인데.”

「그것도 그래.」

뒤이은 거물들의 등장에 쭈구리가 되어 있던 우헤이싱의 눈동자에서 불똥이 튀었다.

「이, 이, 이 빵즈 새끼가!」

“그놈의 빵즈 타령 그만하지. 애국가도 2절부터는 힘들다. 내가 너 봐주는 것도 마찬가지고.”

「……봐줘? 네놈 따위가 나를?」

도무지 이해가 가지 않는다는 말투에 내가 고개를 끄덕였다.

“어. 방금 확실해졌네.”

나는 우헤이싱이 어느 수준인지 짐작하고 있지만, 놈은 내가 어떤 사람인지 조금도 알아차리지 못했다.

싸움은 상대를 가늠하는 것부터 시작이다. 이 싸움은 시작하기도 전에 끝났다.

“그러니까 괜히 시비 걸지 말고 좋게 말할 때 가라. 각자 할 일이나 열심히 하자고.”

「A급 헌터 주제에 주석 동지의 기대를 받는다고 하늘 높은 줄 모르고 나대……!」

“아하.”

왜 초면부터 지랄을 떠나 싶었는데, 이거 때문이었구만. 너무 뻔하고 유치한 이유라 실소가 흘러나왔다.

“거 참. 이걸 귀엽다고 하기에는 나이를 너무 처먹었고.”

「……!」

“어떡하냐? 주석님의 기대와 주목을 한몸에 받고 싶은데, 웬 한국 놈한테 밀려서.”

「너…….」

속마음을 들켰다는 걸 깨달은 우헤이싱의 얼굴이 수치심과 분노로 달아올랐다.

어느새 모두의 이목이 쏠린 상황. 자신을 향한 사람들의 한심한 시선을 놈도 뼈저리게 느끼고 있을 것이다.

그리고 저런 부류의 놈들은 지금 같은 상황이 오면…….

‘꼭, 선을 넘기 마련이지.’

내 예상은 정확히 들어맞았다.

스윽.

검파를 향해 아주 미세하게 미끄러지는 녀석의 손끝.

대범한 샤오 양 주석은 신뢰의 증거로 이 자리의 누구에게도 무장 해제를 부탁하지 않았지만, 그의 배려는 우헤이싱에게 독이 될 것이다.

‘뽑아. 망설이지 말고.’

내가 아무리 막 나가는 것 같아도 최소한의 경우는 따진다.

지금까지는 주석의 요청으로 중국을 돕기 위해 왔으니 참았던 것뿐, 놈이 무기라도 뽑아 들면 적당한 선에서 조질 명분을 얻을 수 있다.

‘그래, 더. 더.’

마치 내게 조종이라도 당하는 것처럼, 우헤이싱의 손길이 검파를 잡아채려던 바로 그때.

저벅. 저벅.

조용하던 지하 벙커의 문밖, 복도에 울려 퍼지는 여러 명의 발걸음 소리.

우헤이싱의 손이 멈추고 굳게 닫혀 있던 문이 열린 것은, 거의 동시에 벌어진 일이었다.

그리고 국방부장 웨이펑후와 함께 등장한 한 사람을 발견한 순간, 내 뇌리에서 우헤이싱의 존재를 깨끗하게 잊혔다.

“내가 너무 늦었군. 많이들 기다렸나?”

붓으로 그린 듯한 굵은 이목구비와 옷으로도 숨길 수 없는 단단한 체구.

이제 고작 40대 초반인 중년인의 모습을 하고 있지만, 가죽 안에 숨은 것은 늙은 호랑이요, 교활한 뱀이다.

‘이정룡.’

나와 눈이 마주친 이정룡의 입가에, 진한 웃음이 맺혔다.
```

## Final English reading copy

```markdown
# Chapter 385

“Isn’t that right, you peninsula bangzi?”[^1]

“What are you saying, you mainland chink bastard?”

A heavy silence descended.

Even while using translation magic, the foreigners like Magic Johnson looked bewildered because they didn’t understand exactly what *bangzi* and *chink* meant. Team Leader Choi clicked his tongue softly, while one man’s face hardened like stone.

“What?”

“What, asshole?”

“Say that again, bangzi.”

“Yeah. Chink.”

“You fucking—”

“Fine. Let’s get this straight. I’m a dog. You’re a chink.”

“……!”

I watched his face twist violently. Just as he was about to shove back his chair and leap to his feet, the woman sitting beside him raised a hand to stop him.

“Enough.”

She was a beautiful woman in her early twenties, with an atmosphere as clean and refreshing as a soft drink. A calm voice continued from between her lips.

“I’d appreciate it if you both toned it down.”

*Stop, huh…*

I stared at her for a moment, then shrugged.

“Sure, if you insist.”

Perhaps my unexpected answer had caught her off guard. Her eyebrows curved slightly.

“I heard you weren’t the sort of person who was easy to deal with, but you’re accepting it more readily than I expected.”

“I have to accept it. It’s your request, after all.”

“You fell for the beauty trap? Ah, this is why being pretty is such a hassle.”

When she nonchalantly swept back her long hair, I let out a quiet laugh.

“Did you just laugh?”

“You seem more interesting than I expected, Ms. Pai Chen.”

Pai Chen. That was her name.

I couldn’t let myself be fooled by the looks and atmosphere of someone who could have been a university cover model. She might not have married, but she was well past fifty.

At the same time, she was an impossibly senior Senior to me—and one of the heroes of the Great Cataclysm.

“So you knew from the beginning. Hmm. I thought kids these days might not know me.”

That wasn’t wrong. Compared to other S-rank Hunters, Pai Chen had definitely appeared in the media far less often.

Behind the scenes, it wasn’t uncommon to hear that she had assumed a new identity and begun a new life.

But I had known about her since I was very young.

“My mother’s been a fan of yours for years. You starred in that romance movie that came out about twenty years ago, didn’t you?”

“Oh my? When was that? Still, it’s nice to meet someone who remembers.”

“Would it be all right if I came to get your autograph sometime? I think my mother would love it if I brought her one from you.”

“Of course. And from now on, just call me Chen. Your full name sounds too stiff. You can call me *older sister* if you want to be more casual.”

“Excuse me? What are you talking about? I searched online, and it says you’re five years older than my mother.”

“……You really aren’t easy to deal with. Just as I heard.”

But there was someone else who was truly not easy to deal with.

“You fucking turtle-dick…!”

His voice boiled over. The man who had briefly been forgotten amid our conversation glared at me with furious eyes.

“How dare a weak-country bangzi look down on me? Do you even know who I am?”

“……Wow. That’s a really shitty line.”

Pai Chen rested her chin on her hand, looking back and forth between us with interest.

“Indeed. I’ve been wondering since earlier—do you even know who this young man is?”

Pai Chen wasn’t the only one who wanted to hear my answer.

Everyone except Team Leader Choi, whose face had taken on an expression of near enlightenment, was staring at my mouth.

The man huffing and puffing like a seven-year-old who had lost an argument, Magic Johnson, America’s Archmage, and even the young man from Britain. Their attendants were no exception.

Under everyone’s gaze, I nodded.

“Of course I know. Wu Heixing.”

He ranked first or second even among S-rank Hunters when it came to media exposure, so there was no way I wouldn’t know him.

At my answer, the man who had been picking a fight with me about bangzi since earlier—Wu Heixing—widened his eyes.

“You knew who I was, and you still acted that way?”

“Even a stray dog passing by would know there’s one complete piece of human trash among the S-rank Hunters.”

“W-What did you say?”

“Why? You didn’t know that your hobby is getting attention and your specialty is committing crimes, then working the media afterward?”

“……!”

“Come to think of it, didn’t you cause trouble last year? You uploaded a raid photo on your official social media with some bullshit about ‘the only drug my country allows me.’ Then a month later, you got caught taking actual drugs. Was it marijuana?”

“Mr. Jin Taekyung.”

“Team Leader Choi, don’t stop me.”

“It wasn’t marijuana.”

“Huh?”

Team Leader Choi cut in abruptly and calmly corrected the Taekyung Wiki.

“It was cocaine and methamphetamine.”

“Oh. I see. Thank you for letting me know.”

“You’re welcome. Now that things have come this far, is there anything left that can’t be said?”

Look at that expression of enlightenment.

Leaving Team Leader Choi behind as he seemed to be giving up on everything and preparing to ascend to immortality, I continued speaking to Wu Heixing with a broad smile.

“Damn, how did you think of setting up foreshadowing like that? This bastard is Wu Heisunwon at minimum. *Purple Raid.*”

“W-What did you say?”

“Come to think of it, there’s another one. Five years ago, you got caught sexually assaulting someone after drugging them at some club called Burning Moon. How did you get acquitted? Under Chinese law, for something like that, it wouldn’t have been strange if you’d been executed two or three times.”

“……!”

“I heard rumors that you’re the son of someone in the Communist Party’s highest ranks. Did you buy your way out with money and power? What a clever little bastard.”

“Sh-Shut your mouth! How dare a bangzi from a lowly background speak to me like that!”

Wu Heixing’s face flushed bright red as he shouted. Then someone who had been quietly watching the entire situation opened his mouth.

“You’re being loud.”

An arrogant voice flowed smoothly through the room.

“You’re frivolous and vulgar. I hear you’re descended from a Chinese aristocratic family, but did the elders of your household never teach you proper etiquette?”

Wu Heixing bit his lip when he recognized the owner of the voice.

“Y-You’re……”

“You’re?”

Beneath neatly groomed brown hair, faintly green eyes slowly swept over Wu Heixing before moving away.

“William.”

At the young man’s call, a middle-aged man with half-gray hair stepped forward from behind him.

His shoes were spotless, and his suit had been pressed as sharply as a blade. Standing tall as he surveyed the room, the middle-aged man spoke in a pleasingly deep voice.

“Everyone, rise and pay your respects to His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle.”

*The Duke of Cambridge and the Earl of Strathearn… Fuck, why does he have so many titles?*

Whatever the case, Prince Felix-whatever added one stern remark.

“Everyone, just call me His Royal Highness Prince Felix.”

“……”

“……”

Look at everyone’s faces. They looked more uncomfortable than anyone else in the world.

Of course, the most spectacular reaction belonged to Wu Heixing, who had just called me a lowborn commoner.

And that was only natural. When it came to social status, how could he possibly beat a member of the British royal family?

“S-So, this is…”

“Ah.”

Prince Felix looked at the flustered Wu Heixing and nodded as if he had just understood.

“I see. Are you a stutterer?”

“A st-stutterer?”

“If not, why can’t you speak properly? Did your family fail to provide you with speech training?”

Long live His Royal Highness the Prince.

I didn’t even have to step in myself. The third in line to the British throne was injecting carbonation straight into me, and I could feel it fizzing all the way down to my duodenum.

I was grinning so hard my mouth felt ready to split open when Prince Felix’s gaze suddenly turned toward me.

“You.”

“Hm? Are you talking to me?”

At my question, the middle-aged man standing behind Prince Felix opened his mouth.

“When His Royal Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Garter, and Knight of the Thistle, addresses you—”

“That will do, William.”

Prince Felix raised a hand and cut off the parrot. Then he gazed at me with benevolent eyes.

“I have personally stepped forward like this, abandoning my dignity, because I have always believed that we must overcome the divisions between social classes.”

“……?”

“What does it matter whether one is a commoner or a noble? We are all simply equal people beneath God. So don’t take that man’s words too much to heart.”

*What the fuck was this supposed to mean?*

I was momentarily at a loss for words when Team Leader Choi whispered discreetly.

“I believe he thinks you’re a commoner.”

“……!”

*Is that prince bastard insane?*

As I stared at Prince Felix with an incredulous expression, he slowly rose from his seat and extended the back of his hand toward me as if it were the most natural thing in the world.

“Well, come along.”

“……Come along? What is it this time?”

The middle-aged man—whether he was a secretary or a parrot, I couldn’t tell—spoke with a pleased smile.

“Kiss the back of his hand and express your gratitude for the benevolence His Royal Highness Prince Felix Alexander Louis has shown you.”

“……”

*Are these people complete lunatics?*

*Did these eighteenth-century fuckers all arrive here in a time capsule?*

Just as my head began to throb, a message spell from Team Leader Choi reached my ear.

- No.

I replied through Sound Transmission.

- What do you mean, no?

- In any case, no. Just smile and let it pass. Prince Felix is famous for being a bit of an oddball.

- If I break the back of his hand right now, wouldn’t he become even more famous?

- No. Absolutely not!

- Just the back of his hand. Or maybe one finger.

- I said no!

I hadn’t known Message Magic could carry this much emotion. Team Leader Choi must have been desperate in his own way.

*Fine. He’s a British prince. It can’t be helped.*

I was trying to swallow my anger when—

“Hey, Sibeol-jwa.”

*What now?*

I looked warily at Magic Johnson, who had suddenly approached me.

I hadn’t expected much from Wu Heixing, who was famous for his anti-Korean sentiment and various scandals in the first place. But the joy of seeing the S-rank Hunters I had only watched on television was gradually running out.

“……No, please. Call me by my name instead of Sibeol-jwa. Would you like it if I called you Fuckson instead of Johnson?”

“Hmm. Now that you mention it, I see your point. Then, Jin?”

“That’s much better. But why?”

“It’s nothing special. You’re not thinking of kissing the prince’s hand, are you?”

*That sounds pretty special to me.*

Taken aback, I immediately asked,

“Of course not. What is this, the Middle Ages? Would you want to if you were me, Johnson?”

“I would.”

“What?”

A flash of enlightenment struck my mind.

I had completely forgotten. Magic Johnson was an American national hero—and the nation’s gay icon.

Time magazine’s pick for *the world’s most influential LGBT person* was now making a serious proposition to me.

“So, I was thinking I’d like to thank the prince on your behalf.”

“……”

What a way to dress it up.

But unlike Magic Johnson, Prince Felix quietly withdrew his hand.

“We are all equal human beings beneath God. This antiquated etiquette must disappear. Magic Johnson, I will accept your kind offer at a later time.”

“……”

*Was that really something the bastard who had just held out his hand to me could say?*

Pai Chen had been listening too. Apparently unable to believe it, she muttered,

“Oh my. He’s shameless. He may be one step above Wu Heixing, despite not having committed any crimes.”

“Even so, he’s still better than Wu Heixing. That one should have been executed under the law.”

“That’s true.”

Spark flew from Wu Heixing’s eyes as he shrank beneath the arrival of one powerful figure after another.

“Th-this, this, this bangzi bastard!”

“Enough with the bangzi routine. Even the national anthem gets hard to get through after the second verse. Me going easy on you is the same.”

“……Going easy on me? You? On me?”

His tone made it clear that he genuinely couldn’t understand. I nodded.

“Yeah. It just became obvious.”

I had a pretty good idea what level Wu Heixing was at, but he hadn’t realized in the slightest who I was.

A fight began with gauging one’s opponent. This fight had ended before it even began.

“So stop picking fights for no reason and leave while I’m still asking nicely. Let’s each focus on doing our own jobs.”

“You’re just an A-rank Hunter, but because Comrade Chairman expects great things from you, you’ve forgotten your place and started running wild—!”

“Ah.”

I’d wondered why he had been acting like an asshole from the moment we met. So that was what this was about.

The reason was so obvious and childish that a dry laugh escaped me.

“Still, calling it cute would be a stretch. You’re too damn old.”

“……!”

“What are you going to do? You want all of the Chairman’s expectations and attention for yourself, but some Korean guy has edged you out.”

“You……”

Wu Heixing’s face flushed with shame and fury as he realized I had seen through his thoughts.

By then, everyone’s attention had gathered on us. He must have been keenly feeling the contemptuous looks everyone was giving him.

And people like him always crossed the line when put in a situation like this.

*They always do.*

My prediction was exactly right.

A faint movement.

His fingertips slid almost imperceptibly toward the hilt of his sword.

The magnanimous Chairman Xiao Yang hadn’t asked anyone present to disarm as a sign of trust, but that consideration would be poison to Wu Heixing.

*Draw it. Don’t hesitate.*

No matter how reckless I might seem, I still weighed the circumstances at least a little.

I had held back until now only because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have grounds to rough him up within reason.

*That’s it. A little more.*

As if he were being controlled by me, Wu Heixing’s hand reached for the hilt. Just as he was about to seize it—

Thud. Thud.

Several sets of footsteps echoed through the hallway outside the quiet underground bunker.

Wu Heixing’s hand stopped, and the tightly shut door opened at almost the exact same moment.

The instant I saw the person who entered alongside Minister of Defense Wei Penghu, I completely forgot that Wu Heixing even existed.

“I’m too late. Have you all been waiting long?”

Bold features that looked as though they had been painted with a brush, and a solid build that even his clothes couldn’t conceal.

He looked like a middle-aged man barely into his forties, but hidden beneath that skin were an old tiger and a cunning snake.

*Lee Jungryong.*

When Lee Jungryong’s eyes met mine, a deep smile formed at the corners of his mouth.

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```
