<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0384.txt",
      "sha256": "6eb54f0157b75e3bccf512101b0943f4dd1f1a75bb80617e6ffe9f24c3218781",
      "bytes": 14681
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f242a095e963a3c8518ef70310869f9bc9f5efc776436dd7108abc18faba3748",
      "bytes": 14828
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "99b7e766ba6a6ea34b0c3dea724329ccd654f567f27d7f5baa9682d03e89d156",
      "bytes": 10838
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c7447866416335350a3dc657f12dab3bf4ae978719a43aa2ff876fcc4dc8b86c",
      "bytes": 23777
    },
    {
      "path": "characters/Wei Penghu.md",
      "sha256": "4bac9c910b4a53e51a6bb9ed3e9613d039d67db572cc1153553eca2b524d474a",
      "bytes": 607
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2687df93ab32feccc172415350902ac495caae475e645f461f1545bb3d12089b",
      "bytes": 6244
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 17312
}
-->

# Durable State Update — Chapter 384

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 384. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 384. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 384,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 384,
    "continuity_sources": [384],
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
    "By the end of the source-only bridge, Jin Taekyung had reached the Supreme Peak realm and Level 120; Chapter 382 grants him another level up, but the resulting level, exact current Fame, complete Titles, martial-art stages, and unassigned points are not stated.",
    "Jin Mukyung is Taekyung's second older brother, twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and substantially stronger than Taekyung.",
    "Dark Heaven rescued the former conspirators from the Demonic Cult, implanted gu in them, and its larger purpose and reason for sparing Taekyung remain unresolved.",
    "The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by the recent Dark Heaven attacks; Tang Sadok has awakened and is again serving as Family Head of the Sichuan Tang Clan.",
    "Tang Sadok confessed that he revealed the Myriad Poison Ring's location to the Western Heaven Demon Lord to preserve the Tang Clan; Taekyung forgave him, and the Tang Clan owes Taekyung's group a great debt.",
    "Taekyung completed the Hidden Quest Atonement and Forgiveness and acquired the Benefactor of the Tang Clan Title, along with EXP, Fame, and a level up.",
    "The Myriad Poison Ring was transferred to Taekyung by Tang Sadok and is now bound to him; White Flame, Myriad Poison Ring, and Flame Dragon Armor are currently bound.",
    "Mungyeong is the Divine Physician and the Slaughter Saint. He has left the Murim's affairs behind, intends to live as a physician, and is the master of Dongbong.",
    "Dongbong is Mungyeong's longtime disciple and a physician who lost his wife and two children to an epidemic before Mungyeong cured him and accepted him as a disciple.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung has successfully completed Logout and returned to the modern world aboard a private jet sent by China's Central Committee toward Chengdu International Airport.",
    "Cheongpung is Mimi's temporary guardian while the Tang Clan's future is uncertain.",
    "The Divine Physician, referred to in Taekyung's joke as Dongbong, has asked Taekyung for time before his departure; the request remains undisclosed.",
    "Dongbong predicts that a great war will soon occur and asks Mungyeong to prevent it as the Divine Physician; Mungyeong verbally refuses and says the Murim is not where he belongs, while the announced departure from Chengdu's western port remains unresolved.",
    "Taekyung and Cheongpung were preparing to leave Sichuan by fast ship from Chengdu's western port after the Hour of the Dog.",
    "Mu Song is the boatman associated with the water bandits preparing the ship.",
    "An unidentified boy reaches the port immediately before departure and is accepted as one more passenger.",
    "The Sichuan Governor's favorite concubine Ae-hyang manipulated him into concealing the government uniforms and weapons involved in the recent martial-artist conflict and preparing a false memorial that exaggerates his role in restoring order. A sinister red light entered her eyes, and she appears to serve an unidentified superior.",
    "Chengdu International Airport is under attack by monsters, with humans and monsters fighting on the ground while around a dozen A-rank wyverns pursue Taekyung's private jet.",
    "Taekyung concludes that the Lich, the supreme undead monster associated with the recent monster wave, has extended its reach to Chengdu.",
    "Team Leader Choi accompanies Taekyung, trusts him to resolve the attack, and can create a pressure-blocking barrier with a ring.",
    "Taekyung cuts an opening in the aircraft with sword qi, called an Aura Blade in the modern world, and kills the lead wyvern and multiple others with a spear.",
    "Shao Shen is a twenty-year-old, Senior Colonel, spear-wielding Hunter of the Public Security Armed Forces who rallies Chinese forces at Chengdu International Airport and admires Taekyung.",
    "Yao Wei was an A-rank Hunter, Shao Shen's friend and comrade, and a playful sparring partner before being killed and reanimated as a Dullahan.",
    "A monster army unexpectedly attacks Chengdu International Airport, including low- and high-level monsters, A-rank flying monsters, and a green wyvern capable of using Poison Breath.",
    "Dark magic spreads through battlefield blood and corpses, restores the dead with strength and souls, and binds the resulting undead to invisible chains.",
    "The three beings controlling the undead army are former human necromancers inhabiting dead mage bodies; their individual identities and origins remain unknown.",
    "The Arch Lich is the superior who sent the three beings to kill humans and create more undead. Whether it is the same entity as the Lich previously associated with the monster wave remains unresolved.",
    "Taekyung and Team Leader Choi arrive at the airport aboard the burning private jet. The plane sweeps through roughly half of the monster army and stops near Shao Shen; Choi's barrier magic keeps the occupants alive, though they are unconscious.",
    "Shao Shen recognizes Taekyung as Sibeol-jwa, the Korean Hunter he had seen in the news, and addresses him as Teacher Jin.",
    "Taekyung completes the unexpected Quest Unexpected Assault after routing the monster army and receives the Undead Hunter Title, considerable EXP and Fame, and one level up.",
    "Taekyung confirms that nearly half of the approximately two-thousand-monster army is undead and that the undead lack life force. He fights them with Scorching Yang Qi, White Flame, Flame Divine Palm, and Flame-Annihilating Divine Fist.",
    "The Skeleton Warlord says the undead are being controlled by someone whose control is weaker than his own and believes the Lich from Taekyung's holographic video probably did not personally participate.",
    "The Skeleton Warlord's chant causes the undead monsters engaged in battle to stop moving, proving that he can influence the army.",
    "The Skeleton Warlord can seize control of nearby undead monsters, make them attack their former allies, and expand the controlled force to roughly two hundred undead.",
    "The Skeleton Warlord's strength is unusually high at Chengdu International Airport because an unexplained surge of mana is flowing through the area.",
    "The three beings have not fully transformed into Liches because one week was insufficient to absorb the death energy required for the transformation.",
    "The three beings combine their power, kill People's Liberation Army soldiers to strengthen the monster army, and deploy or plan to deploy Skeleton Mages, strengthened ogres, Dullahans, and a Death Knight.",
    "Taekyung destroys the undead units sent against him and reaches the three beings before their Death Knight plan can be completed.",
    "The three beings claim to be Arch Liches and swear upon the River of Death that their account of the preceding week is truthful.",
    "Taekyung destroys all three beings: he kills one with Extreme Yang energy, and the Skeleton Warlord consumes the remaining two's death energy.",
    "The Skeleton Warlord absorbs a massive quantity of death energy and becomes much stronger than when Taekyung first encountered him.",
    "Wei Penghu is a Senior General and the Minister of Defense at the Central Military Commission, and the current chairman's right-hand man. He meets Taekyung after the airport battle and arranges a state-guest jet for Taekyung and Team Leader Choi.",
    "Wei Penghu treats Taekyung and Team Leader Choi as state guests of China and provides five fighter aircraft as escorts.",
    "Sichuan Province is in a wartime state, with magical interference disrupting communications and flying monsters attacking frequently.",
    "China has more than ten times as many Gates as other nations and has managed them rigorously since the Great Cataclysm because it was among the countries most severely affected.",
    "The current monster wave began in Gaoping District, Nanchong City, after a sudden mana surge. Authorities received the report thirteen minutes after the first sign appeared.",
    "Lei Fei is a previously undisclosed Chinese S-rank Hunter and commander of the Public Security Armed Forces stationed in Sichuan Province. He disappeared with the Hunters under his command one week earlier, and his death has not been confirmed.",
    "Lei Fei is Wei Penghu's only nephew. Lei Fei's mother died in childbirth, and Wei raised him as his own son.",
    "Wei Penghu asks Taekyung to bring Lei Fei to him if Taekyung finds him. Taekyung agrees but cannot guarantee that Lei Fei is alive; Wei says he needed a thread of hope rather than a guarantee.",
    "Wei Penghu's jet lands at the temporary operations headquarters on Mount Qingcheng."
  ],
  "continuity_sources": [
    383
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved.",
    "The matter the Divine Physician wants to discuss with Taekyung before his departure remains unresolved.",
    "The identity of the boy who arrives at the port and whether he will accompany Taekyung's group remain unresolved.",
    "Whether Mungyeong will ultimately intervene in the coming war or leave the Murim remains unresolved.",
    "The identity of Ae-hyang's superior and the nature of her sinister red-eyed influence remain unresolved.",
    "Whether the Sichuan Governor submits the false memorial and what consequences follow remain unresolved.",
    "The Lich's exact role in the Chengdu attack and the extent of its reach remain unresolved; the Skeleton Warlord believes the Lich did not personally lead this attack.",
    "Whether the Arch Lich is the same entity as the previously referenced Lich remains unresolved.",
    "The individual identities and origins of the three former necromancers controlling the undead remain unresolved.",
    "Whether the Skeleton Warlord's increased power persists, and the full extent of that increase, remain unresolved.",
    "Lei Fei's fate and the fate of the Public Security Armed Forces Hunters who disappeared with him remain unresolved.",
    "The identities of the people waiting at the Mount Qingcheng operations headquarters and the purpose of the meeting remain unresolved."
  ],
  "safe_through": 383,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context.",
    "Render 사죄와 용서 as Atonement and Forgiveness, 당문의 은인 as Benefactor of the Tang Clan, 백염 as White Flame, 동봉 as Dongbong, and 신의 as Divine Physician.",
    "Render 인산인해 as “a sea of people.”",
    "Render 홍무 as Hongwu and 성도 as Chengdu.",
    "Render 술시 as the Hour of the Dog, with a footnote identifying it as a traditional period roughly corresponding to 7–9 p.m.",
    "Render 선화아 as boatman and 무송 as Mu Song.",
    "Retain Master for 스승님 and render 살귀 as slaughter demon in Mungyeong's self-description.",
    "Render 식경 as sikgyeong, approximately thirty minutes, with a footnote.",
    "Render 흑룡갑 as Black Dragon Armor, 화룡갑 as Flame Dragon Armor, 수룡채 as Water Dragon Stronghold, 열화신공 as Blazing Flame Divine Art, 상산왕 as King of Shangshan, and 삼공 as Grand Councilor.",
    "Render 최 팀장 as Team Leader Choi, 리치 as Lich, 스켈레톤 워로드 as Skeleton Warlord, 샤오 양 as Xiao Yang, 중국 중앙위원회 as Central Committee of China, 쓰촨성 as Sichuan Province, 청두 국제공항 as Chengdu International Airport, 헌터 마켓 as Hunter Market, and 검은 별 as Black Star.",
    "Render 와이번 as wyvern, 드레이크 as drake, 용족 as dragonkin, 브레스 as Breath, 강기 as sword qi, and 오라 블레이드 as Aura Blade.",
    "Retain a footnote explaining 빵즈 as a derogatory Chinese slur for Koreans.",
    "Render 샤오 쉔 as Shao Shen, 야오위 as Yao Wei, and 류인친 as Ryu Inchin.",
    "Render 공안 무력부 as Public Security Armed Forces, 인민 해방군 as People's Liberation Army, 중화인민공화국 as People's Republic of China, 중화 as Zhonghua, 오성홍기 as Five-Star Red Flag, and 듀라한 as Dullahan.",
    "Render 시벌좌 as Sibeol-jwa, 중앙 군사 위원회 as Central Military Commission, 화염신장 as Flame Divine Palm, and 멸염신권 as Flame-Annihilating Divine Fist.",
    "Render 염화일로 as Flamefire Path, 아크 리치 as Arch Lich, 데스나이트 as Death Knight, and 스켈레톤 메이지 as Skeleton Mage.",
    "Render 의념 as exchanged thoughts and 사기 as death energy in the three beings' viewpoint scene.",
    "Preserve the pseudo-incantation wordplay for the names of Valencia, Madrid, Bayern Munich, and Stoke City, and for annyeonghaseyo and Yeonye-ga Junggye.",
    "Render 골골이 as Boney as the Skeleton Warlord's teasing pet nickname.",
    "Render 죽음의 강 as River of Death, 검은 숲 as Black Forest, 언데드 헌터 as Undead Hunter, 국방부장 as Minister of Defense, and 상장 as Senior General.",
    "Render 오르페우스 폰 막시무스 발렌시아 바이엘른 as Orpheus von Maximus Valencia Bayern.",
    "Render 레이페이 as Lei Fei, 난충시 as Nanchong City, 가오핑구 as Gaoping District, and 청성산 as Mount Qingcheng.",
    "Render 대교 as Senior Colonel.",
    "Render 국방부장 동지 as Comrade Minister of Defense, 견마지로 as humble strength, 옥체 as august person, and 추웅! 성! as “Loya-alty!” to preserve the comic split-salute wordplay.",
    "Preserve the Pingping/Pengpeng chairman-name joke without identifying the deceased chairman beyond the source."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 생도     | **cadet**                                    |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 사천     | **Sichuan**            |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |
| 청성산 | **Mount Qingcheng** | Mountain containing the temporary operations headquarters. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 382
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Wei Penghu.md

# Wei Penghu (웨이펑후)

- **Safe through:** Chapter 383
- **Aliases:** None
- **Role:** Senior General and Minister of Defense at the Central Military Commission
- **Personality:** Courteous, composed, and direct in his first meeting with Jin Taekyung
- **Voice:** Formal and respectful
- **Relationships:** Meets Jin Taekyung after the Chengdu International Airport battle, brings him toward the temporary operations headquarters, and is Lei Fei's uncle; he raised Lei Fei as his own son and asks Taekyung to bring him back if found.

## Korean source

```text
＃384화



청성산(靑城山).

아득한 세월을 간직한 도교의 성지.

그 준엄하고도 압도적인 산세를 마주한다면, 그 누구라 해도 순간 할 말을 잃고 바라보게 된다.

그러나 나는 전혀 다른 의미에서 놀라움을 느끼고 있었다.

‘분명 다르지만…… 닮았어.’

무림의 청성산. 그리고 21세기 현대의 청성산.

지금껏 내가 경험해 온 두 세상은 많은 부분을 닮았다. 무림에서의 지형, 언어, 사람들의 용모와 생활 양식까지.

한때는 어쩌면 무림은 현대의 머나먼 과거가 아닐까, 고민한 적이 있을 정도였다.

‘하지만 아니었지.’

나비효과? 영화에서나 보던 일이 일어났을 리가.

두 세상은 분명 닮았지만, 미묘한 차이가 있었고 역사도 달랐다.

또한 무림의 세상은 현대의 그것보다 좁고 오대양 육대주로 갈라져 있지도 않다.

이역만리의 이국땅에 색목인들이 살기는 하나 그뿐. 거대한 대국의 통치 아래 존재하는 대륙이 저쪽 세상의 중심이다.

중국 사람들이 지겹도록 주장하는 중화(中和)가 곧 무림일지도 모르겠다.

‘그런데 하필이면 이런 것까지 닮았냐.’

사천성을 무자비하게 피로 물들였던 삼문혈사(三門血史)를 겪고 돌아오자마자 쓰촨성의 청성산에 오다니.

단순한 우연인지, 지독한 악연인지 모르겠다.

부디 그런 것까지 닮진 않았으면 좋겠는데…….

「진 선생?」

“진태경 씨.”

“아.”

나는 잠에서 깨어난 사람처럼 고개를 쳐들었다.

어느새 비즈니스 제트기에서 내린 웨이펑후와 최 팀장이 나를 묘한 눈빛으로 바라보고 있었다.

“죄송합니다. 경치에 잠깐 한눈팔려서.”

「이토록 어두운데 청성산의 절경을 볼 수 있다니. 진 선생께서는 대단한 마나의 소유자시군.」

그것도 틀린 말은 아니지만, 초절정의 경지에 오른 지금은 굳이 공력 없이도 어지간하면 안력(眼力)으로 꿰뚫어 볼 수 있다.

내가 미묘한 얼굴로 고개를 끄덕이자 웨이펑후가 감탄했다.

「과연, 한국이 진 선생을 왜 그리 꼭꼭 숨겨 두었는지 이제야 알 것 같구려. 나라의 얼굴이라 할 만한 S급 헌터답소이다.」

“예? 저 아직 자격증으로는 A급인데요.”

「굳이 숨길 필요 없소. 본국에서도 어느 정도는 파악하고 있으니.」

뭐라 말하기도 전에 웨이펑후가 청산유수처럼 말을 이었다.

「S급 헌터가 되기 위해서는 끊임없는 정신 수양과 고된 수련을 통해 깨달음을 얻어야 하는 법. 본국도 수많은 시행착오를 겪어 가며 지금의 헌터들을 육성했는데…… 진 선생처럼 젊은 나이에 그런 경지에 올랐다는 것은 한국 정부의 전폭적인 지원이 있었다는 뜻이겠지.」

“……?”

“……?”

「아, 물론 옆에 계신 최 선생도 훌륭한 헌터요. 이런 분들이 함께하니 나로서는 든든할 뿐이오.」

이게 무슨 든든하게 국밥 말아먹는 소리냐.

짧은 순간 시선을 교환한 나와 최 팀장은 무언의 합의를 보았다.

‘입 다물자.’

‘그냥 갑시다.’

내가 너무 비현실적으로 이 자리까지 올라왔기 때문에 벌어진 해프닝인 듯싶은데, 이미 저쪽에서 붙인 딱지를 굳이 우리 손을 떼 줄 필요는 없다.

당장 이 자리에서 웨이펑후를 납득시키기도 귀찮고.

“음, 약간 오해가 있으신 것 같은데, 때가 되면 제가 차차 말씀드릴게요.”

「오해랄 것 있겠소. 서로 다 사정 아는 처지에.」

“…….”

“…….”

「주석께서도 이미 알고 계신 사안이니, 뵙게 되면 구태여 부정하지 말고 그러려니 하시오.」

알긴 뭘 알아. 나는 피식 웃었다.

‘그나저나 주석이라.’

중화 인민공화국에 존재하는 10억여 명의 인구와 경제, 군사를 한 손에 틀어쥔 왕 같은 존재.

초절정의 경지에 오른 지금에도 현대의 상식이 뿌리박힌 내게 그는 가까우면서도 한없이 먼 존재다.

이번 일이 끝나면 얼굴이나 한 번 볼 수 있으려나?

뭐, 무슨 상관이겠나. 이건 한참 나중에 생각해야 할 문제다.

레이드 수당을 제외하더라도 주급이 무려 백억. 지금의 내게는 손 큰 고용주일 뿐이다. 사람도 구하고, 돈도 버니 일석이조다.

“그렇게 하겠습니다. 뵙게 되면요.”

「좋소. 그럼 뵈러 갑시다.」

“예?”

「내가 말하지 않았나? 지금 지하 벙커에서 기다리고 계시오.」

아니, 이게 도대체 뭔 상황이야.

앞서가는 웨이펑후의 뒷모습을 멍하니 바라보던 나는 최 팀장에게 다가가 빠르게 속삭였다.

“바, 방금 들으셨어요?”

“예, 들었습니다. 하지만 저로서도 좀 의외로군요. 국가 주석이 안전한 베이징을 놔두고 여기까지 오다니. 세간의 평가가 어느 정도 사실인 모양입니다.”

“세간의 평가고 나발이고. 중국 종석이, 종석이가!”

“종석이가 아니라 총서기! 국가 주석이라고!”

「음? 방금 뭐라 하셨소?」

「아무것도 아닙니다. 국방부장님.」

문득 뒤돌아본 웨이펑후를 향해 정중하게 둘러댄 최 팀장이 지금껏 본 적 없는 아주 진지하고 간절한 표정으로 말했다.

“진태경 씨. 주석 앞에서 지금 같은 말실수는 하면 안 됩니다. 아시겠죠? 특히 종석이 얘기는 말도 꺼내지 마세요. 무슨 고등학교 동창 이름도 아니고.”

“어? 어떻게 아셨어요?”

“…….”

방금 최 팀장이 시발이라고 한 것 같은데. 기분 탓이겠지.

나는 깊게 심호흡하며 속으로 중얼거렸다.

‘종석이 아냐. 총서기야. 중국 주석이야.’

태생부터 성골 귀족이었던 최 팀장과 달리 나는 뼛속까지 소시민이다.

평소 중국에 어떤 감정을 품고 있었건 간에, 세계에서 열 손가락 안에 꼽히는 강대국의 지도자를 만난다는 사실에 가슴이 쿵쿵 뛰었다.

‘실수만 하지 말자. 특히 종석이.’

그리고 십 분 후, 나는 깊숙한 지하 벙커에 모인 주요 인물들의 시선을 받으며 중화인민공화국의 지도자와 악수를 나누었다.

「반갑소, 진 선생. 이 늙은이는 중화인민공화국의 국가 주석을 맡고 있는 샤오 양이라 하오.」

좋아, 종석이의 종자도 꺼낼 일은 없다. 한고비를 넘긴 나는 편안한 마음으로 입을 열었다.

“어서 오세요.”

「……?」

“……?”

아, 시벌.



* * *



중국 공산당 중앙군사위원회 주석이자 총서기. 그리고 10억 명이 넘는 인민들의 정점에 선 국가 주석.

샤오 양(Shao Yang).

사람들을 향한 그의 목소리는 부드럽고, 눈빛에는 힘이 실려 있었다.

「여러분도 알다시피, 안타깝게도 나는 군사 전문가도, 뛰어난 장군도 아니오. 일찍이 정치에 몸담아 나이 일흔이 되어서야 작은 뜻을 이룬 협잡꾼일 뿐이지.」

스스로를 협잡꾼이라 지칭하는 말은, 지구에서 네 번째로 거대한 국토와 제일의 인구수를 지닌 국가 수장의 입에서 나온 말이라곤 믿기지 않을 정도로 파격적이었다.

‘이런 뜻이었나? 최 팀장이 말했던 세간의 평가라는 게.’

대충 어떤 사람인지 알 것 같은 느낌이다.

어쩌면 그저 사람들 앞에서 꺼내 든 가면이나 위선일 수도 있다.

하지만 적어도 지금 나를 포함한 모두의 앞에서 말을 이어 가는 노인, 샤오 양 중국 주석에게는 그런 것과는 전혀 다른 종류의 기(氣)가 느껴졌다.

「최선을 다해 주시오. 부디 한 명이라도 더 많은 인민을 구하고, 하루빨리 이 끔찍한 참사를 막아 주시오. 만약 그리 해 주신다면 나는 여러분과 여러분의 나라에 합당한 고마움을 표시하고 이번에 준 도움을 오래도록 기억할 거요.」

사실 저 노인이 어떤 인생을 살아왔고 어떤 정책을 펼치는지 나는 모른다.

다만 자국의 사람들을 구하기 위해 세계 각국에 도움의 손길을 뻗었다는 것에는 큰 점수를 주고 싶다.

「이 늙은이의 말은 여기까지요. 여러분들은 부디 정치와 같은 복잡한 문제는 신경 쓰지 말고, 최소의 희생으로 이 사태를 막을 수 있는 최선의 방도를 찾아 주시길 간곡히 부탁하겠소.」

정치에 일평생을 바친 늙은 정객(政客)은 고개를 돌려 한 사람을 바라보았다.

「웨이펑후 국방부장. 내 오랜 벗이여.」

「예. 존경하는 주석 동지.」

「중앙군사위원회의 전권을 원하나?」

잠시 망설이던 웨이펑후가 무겁게 고개를 끄덕였다.

「그렇습니다.」

「자네라면 그 힘을 잘 사용할 수 있겠지. 하지만 거절하겠네.」

「……주석 동지?」

「회의가 끝나면 명령서를 가져오게. 모든 일의 전권도, 책임도 내가 질 테니.」

순간 중국 종석이가 왜 저러나 싶었는데, 이제 보니 모두 자신이 안고 가겠다는 의지의 표명이었다.

그 광경을 지켜보던 최 팀장이 옆에서 중얼거렸다.

“좋은 리더군요.”

나는 작게 고개를 저었다.

“아뇨. 저한테는 최 팀장님이 최곱니다.”

“진태경 씨…….”

“그러니까 길드 정산 비율 좀 올려 주세요.”

“진태경 씨…….”

같은 말, 다른 느낌.

니 새끼가 그럼 그렇지, 하는 눈빛으로 나를 바라본 최 팀장이 고개를 젓던 그때였다.

「주석께서 퇴장하십니다.」

서기관의 말에 앉아 있던 모두가 자리에서 일어났다. 국가 원수에 대한 최소한의 예우다.

「모쪼록 무운을 비오.」

주석은 이 자리에 있는 한 사람, 한 사람과 눈을 맞추며 말을 건넸다. 물론 나 역시 예외는 아니었다.

그것도 하필이면 맨 마지막에 걸렸다.

「진 선생.」

“……예.”

나를 바라보는 주석의 입가에 희미한 미소가 스쳤다.

「내 진 선생에게 거는 기대가 아주 크오. 비록 서로가 필요로 하는 것을 주고받는 계약이라지만, 어떤 상황에서도 인명을 우선해 주었으면 좋겠소.」

기분 탓인가, 다른 사람들에 비해 유난히 긴 인사말이다. 나는 사람들의 시선을 느끼며 고개를 끄덕였다.

“알겠습니다.”

「부디 꼭 큰 힘이 되어 주시구려.」

그 말을 끝으로 돌아서려던 주석이 멈칫 발걸음을 멈췄다. 그리고 한 마디를 툭 던졌다.

「어서 오시오.」

“…….”

「그럼 이만.」

주석을 배웅하기 위해 동석하고 있던 중국 고위 관계자들이 사라지고, 나는 의자에 털썩 주저앉았다.

‘시벌.’

만약 내가 죽는다면 사인은 수치사다. 설령 몬스터한테 죽는다고 해도 사인은 수치사로 하기로 했다.

‘으아, 으아아아아!’

마음속으로 온 사방을 향해 울부짖는 내 발을 무언가가 지그시 밟았다. 보나 마나 옆에 앉은 최 팀장이 분명했다.

“왜요.”

최 팀장이 작게 헛기침을 내뱉었다.

“크흠.”

“뭐요.”

“크흐흠. 사람들, 사람들.”

“아.”

주위를 둘러본 나는 그제야 깨달았다. 지하 벙커 안, 남녀와 인종이 뒤섞인 십여 명의 사람들이 나를 주시하고 있었다는 것을.

그리고 그중에서도 특히 눈에 띄는 네 사람이 있었다.

‘저들은…….’

중국인 남녀 한 쌍. 그리고 각각 초록빛과 푸른빛을 띤 서양인 사내 둘.

시선을 마주한 것만으로도 느껴진다. 그들의 몸 안에 웅크린 거대한 기운이.

놀랍다기보다는 당연하다는 생각이 앞섰다. 저 네 사람의 정체를 아는 이들이라면 누구나 나와 같을 것이다.

‘S급 헌터.’

존재 자체가 이슈인 사람들. 전 세계에 존재하는 수많은 헌터 중에서도 정점에 선 이들.

TV와 광고에서 지긋지긋하게 보던 얼굴들이 내 눈앞에 있었다.

그리고 지금, 그중 한 사람이 일어나 내게 손을 내밀었다.

「만나서 반가워. 나는……. 아, 혹시 영어를 잘 모르나? 통역 마법을 써 줄 수도 있는데.」

먼저 말을 걸어 줄 거라고는 생각지도 못했다. 나는 얼떨떨한 얼굴로 그가 내민 손을 맞잡으며 대답했다.

“아닙니다. 괜찮아요.”

「오, 이 친구 발음 보게. 미국인이라고 해도 믿겠는데.」

중년의 흑인. 2미터를 훌쩍 넘기는 거구의 그가 푸른 눈을 빛내며 물었다.

「내가 누군지 아는 것 같은데. 안 그래?」

모를 리가 있나. 나는 샤오 양 주석을 마주했을 때보다 더한 떨림을 느끼며 대답했다.

“물론입니다, 매직 존슨(Magic Johnson).”

전 세계에서 오직 세 명만이 부여받은 대마법사의 칭호.

눈앞의 흑인, 매직 존슨은 그 대마법사 중에서도 가장 전투에 특화되어 있다는 워 메이지(War Mage)다.

‘매직 존슨이랑 이야기를 하다니. 살다 보니 이런 날도 다 오네.’

여러모로 오길 잘했다고 생각하는 내게, 세계 최고의 워 메이지가 활짝 웃으며 말을 건넸다.

「하하. 알아봐 주니 고맙군. 사실 나도 전부터 널 알고 있었어.」

“저, 절요?”

「당연하지. 올해 초등학교에 입학한 내 막내딸도 시벌좌를 아는걸.」

“…….”

아니, 저 염병할 별명은 도대체 어디까지 알려진 거야.

시벌좌라는 별명이 영미권에서는 뭐라고 불리려나. 퍽 가이? 퍽 맨?

매직 존슨의 어린 막내딸이 나를 그런 이름으로 알고 있다고 생각하니 하나도 기쁘지 않다.

그리고 기분이 좋지 않은 것은 나뿐만이 아니었던 모양이었다.

「천박하기 짝이 없는 별명이군. 뭐, A급 헌터 나부랭이에게 딱 어울리긴 하지만.」

이제 막 서른쯤 되었을까. 비교적 젊어 보이는 중국인 사내가 비스듬히 팔짱을 끼며 나를 응시했다.

「안 그래, 반도의 빵즈?」

최 팀장이 말릴 틈도 없었다. 이미 내 목소리는 자동 응답기처럼 흘러나온 후였으니까.

“뭐래, 대륙 짱깨 새끼가.”
```

## Final English reading copy

```markdown
# Chapter 384

Mount Qingcheng.

A sacred Taoist site that had preserved the passage of countless ages.

Anyone who faced its stern, overwhelming mountain terrain would find themselves momentarily speechless, staring in awe.

But I was feeling a completely different kind of surprise.

*They’re definitely different… but they look alike.*

Mount Qingcheng in the Murim. And Mount Qingcheng in the modern world of the twenty-first century.

The two worlds I had experienced so far were similar in many ways—the terrain, the language, and even the appearance and lifestyles of their people.

At one point, I had even wondered whether the Murim might be the modern world’s distant past.

*But it wasn’t.*

The butterfly effect? There was no way something I’d only seen in movies had actually happened.

The two worlds were certainly similar, but they had subtle differences, and their histories were different as well.

The world of the Murim was also smaller than the modern world. It wasn’t divided into five oceans and six continents.

People with colored eyes did live in foreign lands thousands of miles away, but that was all. The center of that world was a continent ruled by a vast and powerful nation.

Perhaps the Zhonghua that the Chinese people insisted on so tirelessly was the Murim itself.

*But why did even this have to look alike?*

I had just returned from the Three-Sect Bloodbath, which had mercilessly dyed Sichuan Province in blood, only to come to Mount Qingcheng in Sichuan Province.

I didn’t know whether it was a simple coincidence or a cursed connection.

I just hoped even that wasn’t similar…

“Teacher Jin?”

“Mr. Jin Taekyung.”

“Huh?”

I lifted my head like someone waking from sleep.

Wei Penghu and Team Leader Choi had already gotten off the business jet and were looking at me with strange expressions.

“Sorry. I got distracted by the scenery for a moment.”

“You can see Mount Qingcheng’s beauty in this darkness. You must possess tremendous mana, Teacher Jin.”

That wasn’t entirely wrong, but now that I had reached the Supreme Peak realm, I could see through most things with my eyesight alone, without even using internal energy.

When I nodded with a subtle expression, Wei Penghu exclaimed in admiration.

“Now I understand why Korea has hidden you away so carefully. You truly are worthy of being called an S-rank Hunter—the face of your nation.”

“What? I’m still A-rank according to my license.”

“There’s no need to hide it. Our country has figured it out to some extent as well.”

Before I could say anything, Wei Penghu continued as smoothly as flowing water.

“To become an S-rank Hunter, one must gain enlightenment through constant mental cultivation and arduous training. Our country has also raised its current Hunters through countless trials and errors… Reaching such a realm at your young age means you must have received the full support of the Korean government.”

“…”

“…”

“Ah, of course, Teacher Choi beside you is also an excellent Hunter. Having people like the two of you with us is reassuring.”

*What was this nonsense about feeling reassured? Was he talking about a hearty bowl of gukbap or something?*

Team Leader Choi and I exchanged glances for a brief moment and reached a silent agreement.

*Keep your mouths shut.*

*Let’s just go.*

This seemed to have happened because I had reached this position in such an utterly unrealistic way. But there was no reason to remove the label they had already stuck on us.

Besides, convincing Wei Penghu right here and now sounded exhausting.

“Well, I think there’s been a slight misunderstanding. I’ll explain everything little by little when the time comes.”

“What misunderstanding? We’re both in a position to know the circumstances.”

“…”

“…”

“The Chairman already knows about the matter, so when you meet him, don’t bother denying it. Just accept it.”

*What does he know?*

I let out a quiet laugh.

*Speaking of the Chairman…*

A kinglike figure who held the population, economy, and military of the People’s Republic of China’s billion-plus people in one hand.

Even now that I had reached the Supreme Peak realm, to me—with modern common sense still rooted deep in my bones—he felt both close and infinitely distant.

*I wonder if I’ll get to see his face once this is over.*

Well, what did it matter? That was a problem for much later.

Even without my raid pay, my weekly salary was a whopping ten billion won. To me, he was merely a generous employer.

I could save people and make money at the same time. Two birds with one stone.

“That’s what I’ll do. If I meet him.”

“Good. Then let’s go meet him.”

“What?”

“Didn’t I tell you? He’s waiting in the underground bunker right now.”

*What the hell was going on?*

I stared blankly at Wei Penghu’s back as he walked ahead, then approached Team Leader Choi and whispered quickly.

“D-Did you hear that?”

“Yes, I did. But it’s somewhat unexpected to me as well. For the Chairman of China to leave the safety of Beijing and come all the way here… The public perception of him must be at least somewhat accurate.”

“To hell with public perception. China’s Jongseok—Jongseok!”

“Not Jongseok! The General Secretary! The state chairman!”

“Hmm? What did you just say?”

“Nothing, Comrade Minister of Defense.”

Team Leader Choi politely covered for us when Wei Penghu suddenly glanced back. Then, wearing an extremely serious and earnest expression I had never seen before, he spoke to me.

“Mr. Jin Taekyung. You must not make a slip like that in front of the Chairman. You understand? Especially the Jongseok thing. Don’t even bring it up. It’s not as though you’re talking about the name of some high school classmate.”

“Huh? How did you know?”

“…”

I could have sworn Team Leader Choi had just said *fuck*.

It was probably just my imagination.

I took a deep breath and muttered inwardly.

*Not Jongseok. The General Secretary. China’s Chairman.*

Unlike Team Leader Choi, who had been born into aristocracy, I was a commoner down to my bones.

Whatever feelings I usually had toward China, the thought of meeting the leader of one of the world’s ten greatest powers made my heart pound.

*Let’s just not make any mistakes. Especially not about Jongseok.*

Ten minutes later, I stood amid the gazes of the important figures gathered in a deep underground bunker and shook hands with the leader of the People’s Republic of China.

“Nice to meet you, Teacher Jin. This old man is Xiao Yang, the state chairman of the People’s Republic of China.”

*Good. I won’t even have to utter the first syllable of Jongseok.*

Having cleared the first hurdle, I opened my mouth with a relaxed mind.

“Welcome.”

“…”

“…”

*Oh, fuck.*

* * *

Chairman of the Central Military Commission of the Chinese Communist Party and General Secretary.

And the state chairman standing at the pinnacle of more than a billion people.

Xiao Yang.

His voice was gentle as he spoke to the people gathered there, but his eyes held power.

“As you all know, unfortunately, I am neither a military expert nor an outstanding general. I am merely a political schemer who entered politics early and achieved one small ambition only after reaching the age of seventy.”

The fact that he referred to himself as a schemer was so audacious that it was difficult to believe the words had come from the leader of a nation with the fourth-largest territory and the largest population on Earth.

*Was this what Team Leader Choi meant by the public perception of him?*

I felt as though I had a rough idea of what kind of person he was.

Perhaps it was merely a mask or hypocrisy he had put on before the people.

But at least from the old man continuing to speak before all of us—including me—Chairman Xiao Yang of China, I sensed a kind of qi entirely different from either of those things.

“Please do your utmost. Save as many of our people as possible, and stop this terrible disaster as soon as you can. If you do so, I will express my gratitude to you and your country in a manner befitting your efforts, and I will remember the help you have given us for a long time.”

I knew nothing about the life that old man had lived or the policies he had pursued.

But I wanted to give him considerable credit for reaching out to countries around the world for help in order to save his own people.

“That is all this old man has to say. I earnestly ask you not to concern yourselves with complicated matters like politics. Please find the best way to stop this situation with the fewest possible sacrifices.”

The old politician, who had devoted his entire life to politics, turned his head and looked at one man.

“Minister of Defense Wei Penghu. My old friend.”

“Yes, Comrade Chairman.”

“Do you want full authority over the Central Military Commission?”

Wei Penghu hesitated for a moment, then gave a heavy nod.

“Yes.”

“You would use that power well. But I will refuse.”

“…Comrade Chairman?”

“When this meeting is over, bring me the written order. I will take full authority over every matter and bear all the responsibility myself.”

For a moment, I wondered why China’s Jongseok was acting that way.

But now I understood. It was his declaration that he would shoulder everything himself.

Team Leader Choi muttered beside me as he watched the scene.

“He’s a good leader.”

I shook my head slightly.

“No. To me, Team Leader Choi, you’re the best.”

“Mr. Jin Taekyung…”

“So please raise my Guild settlement percentage.”

“Mr. Jin Taekyung…”

Same words. Different feeling.

Team Leader Choi looked at me as if to say, *Of course you’d say that, you bastard,* and shook his head.

That was when it happened.

“The Chairman is leaving.”

At the secretary’s words, everyone who had been seated rose from their places.

It was the minimum courtesy owed to a head of state.

“I wish you all good fortune.”

The Chairman looked each person in the eyes as he spoke to them.

Of course, I was no exception.

As luck would have it, I was the last one.

“Teacher Jin.”

“…Yes.”

A faint smile touched the corners of the Chairman’s mouth as he looked at me.

“I have very high hopes for you, Teacher Jin. Though this is a contract in which we exchange what we each need, I hope that you will put human lives first in every situation.”

Was it my imagination, or was his farewell unusually long compared to everyone else’s?

Feeling everyone’s eyes on me, I nodded.

“I understand.”

“Please be a great source of strength to us.”

The Chairman finished speaking and was about to turn away when he abruptly stopped.

Then he tossed out one more word.

“Welcome.”

“…”

“Well, that will be all.”

After the high-ranking Chinese officials who had been present to see the Chairman off disappeared, I dropped heavily into a chair.

*Fuck.*

If I died, the cause of death would be humiliation.

Even if a monster killed me, I would insist that the cause of death be recorded as humiliation.

*No! Nooooooo!*

As I screamed inwardly in every direction, something pressed down firmly on my foot.

It was obviously Team Leader Choi, who was sitting beside me.

“What?”

Team Leader Choi gave a small cough.

“Ahem.”

“What?”

“Ahem. People. People.”

“Oh.”

I looked around and finally realized that more than a dozen men and women of different races were watching me inside the underground bunker.

Four of them stood out in particular.

*Those people are…*

A Chinese man and woman.

And two Western men, one tinged with green and the other with blue.

I could feel it just from meeting their eyes—the immense power coiled inside their bodies.

My first thought wasn’t that it was surprising, but that it was only natural. Anyone who knew the identities of those four would have thought the same thing.

*S-rank Hunters.*

People whose very existence was news. Those who stood at the pinnacle of the countless Hunters in the world.

The faces I had seen to death on television and in advertisements were right in front of me.

And now, one of them stood up and extended a hand toward me.

“Nice to meet you. I’m… Ah, do you perhaps not speak English? I can use translation magic if you’d like.”

I hadn’t expected him to speak to me first. Looking flustered, I took his hand and answered.

“No, it’s fine.”

“Oh, listen to this fellow’s pronunciation. I’d believe you if you told me you were American.”

The middle-aged Black man was a giant well over two meters tall. His blue eyes gleamed as he asked,

“You seem to know who I am. Don’t you?”

As if I wouldn’t.

I felt even more nervous than I had when facing Chairman Shao Yang.

“Of course, Magic Johnson.”

The title of Archmage had been bestowed upon only three people in the entire world.

The Black man standing before me, Magic Johnson, was a War Mage—the most combat-oriented of those three Archmages.

*I’m talking to Magic Johnson. I guess days like this really do come along.*

As I thought that I had made the right choice in coming here, the world’s greatest War Mage smiled broadly and spoke to me.

“Haha. I’m glad you recognized me. Actually, I’ve known about you for a while too.”

“M-Me?”

“Of course. Even my youngest daughter, who started elementary school this year, knows Sibeol-jwa.”

“…”

*How far has that damn nickname spread?*

What would they call the nickname Sibeol-jwa in the English-speaking world?

*Fuck Guy? Fuck Man?*

The thought of Magic Johnson’s little youngest daughter knowing me by that name was not flattering in the slightest.

And apparently, I wasn’t the only one who disliked it.

“That is an obscenely vulgar nickname. Though I suppose it suits a mere A-rank Hunter like you.”

A Chinese man who looked to be around thirty, relatively young, stared at me with his arms folded at an angle.

“Isn’t that right, you peninsula bangzi?”[^1]

Team Leader Choi didn’t even have time to stop him.

My voice had already come out like an automatic response.

“What are you saying, you mainland chink bastard?”

[^1]: *Bangzi* is a derogatory Chinese slur for Koreans.
```
