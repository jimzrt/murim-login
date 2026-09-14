<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0383.txt",
      "sha256": "f9e69192a9914b1975fadec7a7462e85e486b529cd60379e7fccf6baad16a594",
      "bytes": 15379
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "243be40faed918076ae146c12b71bae36237535d1065d87864fb9e439ef1ef54",
      "bytes": 12982
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "573b04e7127e9798da31d12c11f31be698526959457ff3a1e3067f70d3d6afcc",
      "bytes": 10081
    },
    {
      "path": "characters/Wei Penghu.md",
      "sha256": "054c9810d4a363a61a6e493f97a7b83f86f18098e23734efd1aada51f28df03d",
      "bytes": 496
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ca6e5b42a138f7591bfb0f4302d08abbbefc0766411bfeb0a476116f455eec00",
      "bytes": 5676
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 16331
}
-->

# Durable State Update — Chapter 383

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 383. Keep at most
2 continuity_sources. Use only chapter
numbers through 383. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 383,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 383,
    "continuity_sources": [383],
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
    "Shao Shen is a twenty-year-old spear-wielding Hunter of the Public Security Armed Forces who rallies Chinese forces at Chengdu International Airport.",
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
    "Wei Penghu is a Senior General and the Minister of Defense at the Central Military Commission. He meets Taekyung with Team Leader Choi and Shao Shen after the airport battle.",
    "A jet is waiting at the operations headquarters, where Wei Penghu says everyone is waiting for Taekyung."
  ],
  "continuity_sources": [
    382
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
    "Whether Taekyung's private jet explodes or can be recovered remains unresolved.",
    "Whether the Arch Lich is the same entity as the previously referenced Lich remains unresolved.",
    "The individual identities and origins of the three former necromancers controlling the undead remain unresolved.",
    "Whether the Skeleton Warlord's increased power persists, and the full extent of that increase, remain unresolved.",
    "The identity of everyone waiting at the operations headquarters and the purpose of the meeting remain unresolved."
  ],
  "safe_through": 382,
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
    "Render 오르페우스 폰 막시무스 발렌시아 바이엘른 as Orpheus von Maximus Valencia Bayern."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 웨이펑후 | **Wei Penghu** | Senior General and Minister of Defense at the Central Military Commission. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 쓰촨성 | **Sichuan Province** | Province containing Chengdu International Airport. |
| 중화인민공화국 | **People's Republic of China** | Country whose flag appears on Shao Shen's armor. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 국방부장 | **Minister of Defense** | Wei Penghu's office at the Central Military Commission. |

## Listed compact profiles

### Wei Penghu.md

# Wei Penghu (웨이펑후)

- **Safe through:** Chapter 382
- **Aliases:** None
- **Role:** Senior General and Minister of Defense at the Central Military Commission
- **Personality:** Courteous, composed, and direct in his first meeting with Jin Taekyung
- **Voice:** Formal and respectful
- **Relationships:** Meets Jin Taekyung after the Chengdu International Airport battle and brings him toward the operations headquarters

## Korean source

```text
＃383화



웨이펑후가 준비해 두었다는 제트기는 생각했던 모습과는 상당한 차이가 있었다.

‘넓네. 화려하고.’

살짝 열린 출입문 너머로 고급스러운 테이블과 소위 말하는 회장님 의자가 보였다.

곁에 있던 최 팀장이 우리가 보고 있는 이게 한 대당 천억에 육박하는 비즈니스 제트기라는 걸 알려 주며 덧붙였다.

「국빈용으로나 쓰이는 기체를 여기서 볼 줄은 몰랐군요.」

웨이펑후가 담담하게 대꾸했다.

「당연한 일이오. 두 선생께서는 본국의 국빈이시니.」

“아.”

「덕분에 수많은 병사와 헌터들을 살릴 수 있었소. 나를 포함한 모두는 오늘의 도움을 절대 잊지 않을 거요.」

“……아, 예.”

그 전에 미세먼지와 역사 왜곡부터 좀 처리해 줬으면 좋겠는데.

내심 중국이 내가 알고 있는 것보다 더 양심적인 국가이길 바라며 기체에 몸을 실었다.

대기하던 조종사가 우리를 향해, 정확히는 웨이펑후를 향해 절도있는 동작으로 경례를 올렸다.

「오셨습니까, 국방부장 동지.」

「준비는?」

「본 기체를 포함한 호위기 모두 준비를 끝마쳤습니다. 명령만 내려 주시면 됩니다.」

호위라기에 뭔 소린가 했더니, 창밖 활주로에 날렵한 곡선을 자랑하는 전투기 다섯 대가 신호를 보내듯 불을 깜빡이는 것이 보였다.

‘뭐여, 저게.’

전쟁 영화에서나 보던 걸 여기서 보네. 당장 한판 뜨러 가기라도 하는 건가?

눈을 동그랗게 뜬 내 모습에 웨이펑후가 입을 열었다.

「아직 외부에는 정확히 알려지지 않았지만…… 알다시피 현재 쓰촨성은 전시 상황이오. 마법으로 인한 통신 방해와 비행 몬스터들의 습격까지 빈번하게 이루어지는 실정이니, 안전을 위해 호위는 필수지.」

“정말입니까?”

생각했던 것보다 상황이 심각하다.

우리야 청두 국제공항을 습격하러 온 와이번에게 겸사겸사 느낌으로 습격을 당한 거지만, 이게 쓰촨성 전역에서 벌어지는 일이라면 이야기가 달라진다.

「차라리 내가 거짓말을 하는 거라면 얼마나 좋겠소.」

현재 상황을 떠올리는 것만으로 지치는지, 부쩍 늙어 버린 웨이펑후가 푹신한 좌석 시트에 몸을 기댔다.

「자네와는 여기에서 작별해야 할 듯싶군. 조만간 다시 만나세. 샤오 쉔 대교(大校).」

우리와 달리 기체에 오르지 않은 한 사람, 샤오 쉔이 부동자세로 경례를 취했다.

「예. 조속히 임무를 마친 후 합류하겠습니다, 국방부장 동지. 그리고 두 선생님.」

「그래, 기대가 크네.」

상당한 전공을 세웠기 때문인지 전도유망한 젊은 헌터를 바라보는 웨이펑후의 입가에 흐뭇한 미소가 스쳤다.

최 팀장은 정중한 묵례로 인사를 대신했고, 나는 손을 흔들어 주었다.

“다음에 또 봐요. 오늘 아주 잘 싸웠어.”

단지 한 마디였을 뿐이었다.

하지만 내 말을 들은 샤오 쉔의 눈동자가 쟁반만큼 커졌다. 전기에 감전된 것처럼 몸을 부르르 떨던 그가 쩌렁쩌렁하게 외쳤다.

「가, 감사합니다! 진 선생님께서 실망하시는 일 없도록 모든 일에 견마지로(犬馬之勞)를 다하겠습니다!」

“……아니, 뭘 견마지로씩이나.”

「옥체 무사하시길 기원하겠습니다! 추웅! 성!」

“옥체라니. 그게 무슨…….”

빡!

「흡!」

“…….”

저건 잘못된 판단의 표본 같은데.

경례를 얼마나 세게 했는지 손날로 본인의 눈썹 부분을 때린 수준이다.

이를 악물고 아픔을 참는 샤오 쉔의 모습을 황당하게 바라보던 그때, 입구가 닫히고 우리가 탄 비즈니스 제트기가 천천히 이륙을 시작했다.

“저 친구도 뭐랄까, 그……. 캐릭터가 독특하네요.”

내 떨떠름한 말에 웨이펑후가 피식 웃었다.

「우상에게 칭찬을 들었으니 그럴 만도 하지 않겠소?」

“예?”

「본국에는 진 선생을 동경하는 젊은 헌터들이 많소. 저 친구도 예외는 아니지.」

뭐야, 나 한류 스타였어?

그나저나 이 양반, 나는 새도 떨어트린다는 포 스타치고 아랫사람에게 관심이 많은 것 같다.

아니면 샤오 쉔이 그만큼 기대받는 청년이거나.

아, 그런데…….

- 팀장님. 중앙군사위원회 국방부장이면 정확히 어느 정도예요? 제가 이쪽 편제를 잘 몰라서.

내 전음에 움찔한 최 팀장이 메시지 마법으로 대답했다.

- 우리나라로 치자면 국방부 장관입니다. 물론 이곳은 중국이고, 웨이펑후는 현 주석의 오른팔이니 그 권력이 훨씬 막대하죠.

- 아.

나랑 비슷하네. 난 국밥부 장관인데.

순대국 특 하나면 공깃밥 세 그릇 정도는 거뜬하다.

물론 웨이펑후는 손가락질 하나로 도시 세 개를 지워 버릴 수도 있겠지만.

그리고 지금, 막대한 권한을 지닌 중화인민공화국의 권력자가 우리를 향해 상반신을 기울이며 묻고 있다.

「가는 동안 나눠야 할 대화가 많은 것 같소만. 안 그렇소?」

최 팀장과 내가 진지하게 고개를 끄덕이며 입을 열었다.

「물론입니다. 우선 현재 쓰촨성의 상황이 정확히 어찌 돌아가는지부터 여쭤…….」

“그런데 혹시 삶은 달걀이랑 사이다 없나요. 열심히 싸웠더니 허기가 져서.”

“…….”

“…….”

없는 모양이다.

「있소.」

“……?”

“……?”

이게 있네.



* * *



중화인민공화국.

중국의 정식 명칭에서 알 수 있듯이 이 위엄 넘치는 대륙인들은 아직도 사회주의를 국가 이념으로 삼고 있었다.

지금으로부터 약 이십여 년 전, 종신 집권으로 독재의 기틀을 공고히 다졌던 당시 주석이 대격변 도중 사망하면서 훨씬 온건한 정권으로 권력이 이양되기는 했지만, 아직도 알맹이는 여전하다.

- 죽은 주석 이름이 뭐였죠? 핑핑이? 팽팽이?

웨이펑후의 말에 맞장구치던 최 팀장이 입술을 달싹였다. 경이로울 정도의 포커페이스다.

- ……혹시나 해서 드리는 말씀인데, 이곳에서 그런 말 꺼냈다가는 정말 큰일 납니다.

- 그래서 전음, 아니 메시지 마법으로 하잖아요.

- 주의하라는 말입니다. A급 이상의 뛰어난 마법사 중에는 메시지 마법을 도청할 수 있는 사람도 있어요.

- 어쨌건 이름이 뭐였죠? 핑핑이, 아니면 팽팽이? 저 이거 못 들으면 오늘 잠 못 자요.

- ……핑핑이.

결국은 대답해 줄 거면서 뭘.

비로소 후련해진 나는 들려오는 웨이펑후의 말에 귀를 기울였다.

「그 누구도 예상치 못한 일이었소.」

쓰촨성은 광활한 면적과 수천만의 인구를 보유한 거대한 성.

그리고 이 모든 일은 쓰촨성에 존재하는 20여 개 행정 구역 중 하나, 난충시의 가오핑구에서 시작되었다.

「알다시피 본국에 존재하는 게이트의 숫자는 타국과 비교하면 열 배 이상 많소. 때문에 대격변 당시 가장 큰 피해를 입었던 국가 중 하나였고, 그만큼 철저하게 관리하고 있었지.」

하지만 사람의 힘으로 천재지변까지 제어할 수는 없었고, 몬스터 웨이브는 천재지변보다 더한 재앙이었다.

「가오핑구에서 마력 수치가 급등했다는 연락을 받은 건, 첫 징후가 나타난 지 정확히 13분이 지난 후였소. 그리고 쓰촨성에 주둔 중이던 공안무력부장 레이페이가 휘하 헌터들을 이끌고 현장에 도착했을 때는…… 모든 것이 늦은 후였지.」

“레이페이?”

낯선 이름. 그러나 어째서일까, 문득 떠오르는 기억이 있었다.

‘출발하기 전, 길드 하우스에서 최 팀장이 보여 줬던 그 영상.’

아직도 생생하다. 홀로그램이 비춘 아비규환의 도시와 헌터들의 선두에서 몬스터들을 베어 가던 한 남자의 모습이.

그의 무기에는 눈이 부실 만큼 찬란한 오라가 맺혀 있었다.

“본 적이 있는 것 같습니다. 혹시 보내 주신 영상에 나왔던 그……?”

「그렇소.」

잠시 머뭇거리던 웨이펑후가 옅은 한숨과 함께 입을 열었다.

「본국이 보유한 S급 헌터 중 한 명이었소. 물론 두 선생께서는 모르시겠지만.」

모를 거라고?

S급 헌터는 전 세계를 통틀어도 스무 명밖에 되지 않는 절대 강자들.

그들이 누리는 유명세와 지위는 무림의 초절정 고수가 가지는 그것보다 훨씬 크고 강하다.

인터넷, 뉴스, SNS가 그들의 발판이고 마이크와 카메라는 그림자처럼 따라붙는다.

무림인을 향한 양민들의 시선이 경계심 반, 호기심 반이라면 현대인들에게 헌터는 그저 선망의 대상이다. 그야말로 세계의 유명인인 것이다.

‘그런데 그런 S급 헌터를 우리가 모른다고?’

웨이펑후는 에둘러 말했지만, 그 말에 담긴 뜻을 알아듣기에는 충분했다.

나와 최 팀장의 시선이 허공에서 부딪쳤다. 이 순간, 우리는 같은 생각을 떠올리고 있었다.

‘드러나지 않은 S급 헌터.’

아니, 정확히 말하자면 중국 정부가 의도적으로 감춘 S급 헌터라고 하는 게 맞겠다.

‘이런 건 소문으로만 들었는데. 사실이었나?’

S급 헌터는 한 국가의 얼굴이나 다름없는 존재.

그러나 얕보이지 않기 위해 안간힘을 쓰는 약자와는 달리, 강자는 오히려 발톱을 감춘다.

이미 두 명의 S급 헌터를 보유하고 있다고 알려진 중국은 모든 힘을 드러내고 싶지 않았던 게 분명했다.

어쩌면 중국뿐만 아니라, 세계 유수의 강대국들도 마찬가지일 것이다.

‘거 참. 대격변을 겪고서도 이런 눈치싸움이라니.’

한심하기도 했고, 한편으로는 이해가 될 것 같기도 하다. 외교, 정치. 내가 알 수 없었던 세상의 진실을 조금이나마 엿본 것 같아 기분이 묘했다.

그리고 그런 나와 달리, 최 팀장은 보다 더 예리한 사람이었다.

「귀국이 보유한 S급 헌터 중 한 명‘이었다’는 건, 과거형으로 들리는군요.」

웨이펑후가 참담한 얼굴로 대답했다.

「……처음 몬스터 웨이브가 일어났던 일주일 전, 레이페이는 실종되었소. 그가 지휘하던 공안무력부의 헌터들과 함께.」

「실종이 확실합니까? 혹시…….」

「죽음은 확인하지 못했소. 그 영상을 마지막으로 리치. 아니지, 아크 리치라 불린 그 몬스터가 마력으로 모든 통신과 감시를 차단했으니까.」

나와 최 팀장은 동시에 침음성을 흘렸다. 우리의 반응에 웨이펑후가 갈라진 목소리로 물었다.

「선생들도 레이페이가 죽었다고 생각하시오?」

“음.”

“어…….”

실종. 그것도 일주일 전에 그 아비규환 속에서 실종되었다면 이미 결말은 정해져 있는 것이나 다름없다.

최 팀장의 눈짓에 나는 조심스럽게 입을 열었다.

“그, 뭐냐. 사람 일은 어떻게 될지 모르는 것이지만…….”

「다른 전문가들은 백 퍼센트 죽었을 거라 하더군. 천하에 쓸모없는 허풍선이들 같으니.」

왜 그래. 진짜 전문가 맞는 것 같은데.

저 상황에서 살아 있다고 장담하는 놈이 있으면 당장 잘라야 한다. 그게 엄연한 사실이니까.

「하지만 내 생각은 다르오. 레이페이, 그 아이는 반드시 살아 있을 거요.」

“저도 그러길 바랍니다만, 아무래도 현실적으로 봤을 때…….”

「하나뿐인 외조카요. 어릴 적부터 병약했던 내 누이는 산고를 이기지 못하고 세상을 떠났고, 젖도 못 뗀 핏덩이를 내가 지금까지 친자식처럼 키웠지.」

“예?”

아니, 외조카라니. 친자식처럼 키웠다니. 이게 뭔 소리야.

석상처럼 굳어 버린 내게 웨이펑후가 축축해진 눈동자로 물었다.

「그런데 뭐라 하려고 했소? 현실적으로 봤을 때, 그 뒤에 말이오.」

시벌, 이건 역대급 위기다.

순간 말문이 턱 막혔던 나는 간신히 목소리를 쥐어짜 냈다.

“그, 현실적으로 봤을 때. 살아 있을 확률도 아주 없진 않다고 말씀을 드리려고 한 건데요.”

「그렇소? 그게 사실이오?」

“아, 예. 하지만 그 확률이라는 게 매우 희박…….”

「고맙소, 진 선생!」

“아니, 장군님. 대장님. 수령님. 잠시만 고정하시고 제 말을 좀 더…….”

덥석!

틀렸다. 웨이펑후는 이미 내 말을 듣고 있지 않았다. 그 대신 눈물이 그렁그렁 맺힌 눈동자로 내 손을 감싸 쥐었다.

「한 가지 부탁해도 되겠소?」

그 부탁, 안 했으면 좋겠는데.

간절한 내 바람과는 달리, 결국 몇 초 후 예상했던 한 마디가 가슴을 파고들었다.

「혹시 나중에 진 선생께서 그 아이를 만난다면 데려와 주실 수 있소?」

“…….”

「내 이리 부탁하리다.」

간절하게 부탁하는 그의 어깨너머로 최 팀장이 고개를 젓는 것이 보인다.

차라리 처음부터 단호하게 대답했다면 어땠을까. 후회했지만 이미 늦었다.

결국 내가 할 수 있는 대답은 하나뿐이었다.

“그렇게 하겠습니다. 하지만…….”

「진 선생.」

“네?”

「굳이 말하지 않아도 되오. 이미 각오하고 있는 일이니.」

“……!”

소매로 눈가를 훔친 웨이펑후는 혈육의 안위를 걱정하는 장년인이 아닌, 중앙군사위원회 국방부장으로 돌아와 있었다.

「이것으로 충분하오. 누구도 선뜻 나서 주질 않았는데, 진 선생이 약속해 주었으니 안심이오.」

“저도 장담할 수는 없습니다.”

「내게 필요한 건 누군가의 호언장담이 아니었소. 실낱같은 희망이었지.」

웨이펑후가 작게 읊조린 그때, 붕 뜨는 부유감과 함께 기체가 지상을 향해 미끄러졌다.

창밖, 짙은 어둠에 휩싸인 그곳에 험악한 산세와 쉴 새 없이 움직이는 불빛, 그리고 군용차량이 보인다.

「도착한 것 같군.」

뭔가에 사로잡힌 사람처럼, 창밖의 풍경을 뚫어져라 바라보던 내가 물었다.

“여기가 어딥니까?”

「임시 작전 본부요.」

“아뇨. 그걸 물어본 게 아닙니다.”

「음?」

“산. 저 산이 왠지 모르게 낯익은 기분이라서요.”

「그럴 리가. 진 선생께선 본국에 입국한 적이 없는 것으로 아는데…… 아, 혹시 사진으로 본 것 아니오?」

“사진이요?”

「유네스코에서 지정한 세계문화유산이니 충분히 가능한 일이지.」

웨이펑후가 옅은 웃음과 함께 말을 이었다.

「임시 작전 본부. 청성산(靑城山)에 온 것을 환영하오.」
```

## Final English reading copy

```markdown
# Chapter 383

The jet Wei Penghu had prepared looked nothing like what I had expected.

*It’s spacious. And fancy.*

Through the slightly open door, I could see a luxurious table and the kind of chair people called a chairman’s chair.

Team Leader Choi, who was standing beside me, informed me that this was a business jet costing close to one hundred billion won per aircraft, then added,

“I never thought I’d see an aircraft normally reserved for state guests here.”

Wei Penghu replied calmly.

“Of course. The two of you are state guests of our country.”

“Oh.”

“Thanks to you, we were able to save countless soldiers and Hunters. No one—including me—will ever forget the help you gave us today.”

“…Ah, yes.”

*I’d appreciate it if you dealt with the fine dust and historical distortions first.*

Hoping inwardly that China was a more conscientious country than I knew it to be, I boarded the aircraft.

The waiting pilot gave us a crisp salute—or, more precisely, gave Wei Penghu a crisp salute.

“Have you arrived, Comrade Minister of Defense?”

“Are we ready?”

“All escort aircraft, including this one, have completed preparations. We are awaiting your orders.”

I wondered what he meant by “escort,” then looked out the window and saw five fighter jets with sleek, elegant curves blinking their lights as if signaling us.

*What the hell?*

I had only ever seen things like that in war movies. Were we heading straight into a fight?

Seeing my eyes widen, Wei Penghu spoke.

“The exact situation has not yet been made public, but as you know, Sichuan Province is currently in a state of war. Magical interference with communications and attacks by flying monsters are occurring frequently. Escorts are essential for our safety.”

“Are you serious?”

The situation was worse than I had imagined.

The wyverns had come to attack Chengdu International Airport and only attacked us while they were at it, but if the same thing was happening throughout Sichuan Province, that was an entirely different story.

“If only I were lying. How wonderful that would be.”

Perhaps merely recalling the current situation was exhausting him. Wei Penghu, who seemed to have aged considerably, leaned back into the soft seat.

“It seems we must part ways here. I hope we meet again soon, Senior Colonel Shao Shen.”

Unlike us, one man had not boarded the aircraft. Shao Shen stood rigidly at attention and saluted.

“Yes. I will complete my mission as quickly as possible and rejoin you, Comrade Minister of Defense. And you as well, Teachers.”

“Yes. I have high hopes for you.”

Perhaps because he had achieved so much, a pleased smile briefly touched Wei Penghu’s lips as he looked at the promising young Hunter.

Team Leader Choi substituted a polite bow for a farewell, while I waved.

“See you next time. You fought really well today.”

It was only one sentence.

But Shao Shen’s eyes grew as large as serving trays when he heard me. His body trembled as though he had been electrocuted, and he shouted in a booming voice,

“Th-Thank you! I will devote every ounce of my humble strength to every task so that Teacher Jin is never disappointed!”

“…No need to go that far.”

“I pray that your august person remains safe! Loya-alty!”

“Your august person? What does that even—”

Smack!

“Ngh!”

“…”

*That looked like a textbook example of a bad decision.*

He had saluted so forcefully that the edge of his hand had struck his own eyebrow.

I was staring dumbfounded at Shao Shen as he clenched his teeth and endured the pain when the entrance closed and our business jet slowly began to take off.

“That friend of yours is, well… What should I say? His character is pretty unique.”

At my dubious comment, Wei Penghu let out a quiet laugh.

“He heard praise from his idol. Can you blame him?”

“Pardon?”

“There are many young Hunters in our country who admire Teacher Jin. He is no exception.”

*What? Was I a Korean Wave star now?*

Come to think of it, this man seemed unusually interested in those beneath him for a four-star general who was powerful enough to make birds fall from the sky.

Or perhaps Shao Shen was simply a young man who inspired that much expectation.

*Ah, but…*

- Team Leader, where exactly does the Minister of Defense at the Central Military Commission sit in the hierarchy? I’m not familiar with how things are structured here.

Team Leader Choi flinched at my Sound Transmission, then answered through message magic.

- In our country, he would be the Minister of Defense. Of course, this is China, and Wei Penghu is the current chairman’s right-hand man, so his power is far greater.

- Ah.

*We’re similar. I’m the Minister of Soup and Rice, myself.*

*One extra-large bowl of sundae-guk[^1] is enough for me to polish off three bowls of rice.*

*Of course, Wei Penghu could probably erase three cities with a single point of his finger.*

And now, that powerful official of the People's Republic of China leaned his upper body toward us and asked,

“We have quite a lot to discuss on the way. Wouldn’t you agree?”

Team Leader Choi and I solemnly nodded and began to speak.

“Of course. First, we would like to ask exactly what is happening in Sichuan Province—”

“By the way, do you happen to have any boiled eggs and soda? I’m hungry after fighting so hard.”

“…”

“…”

Apparently, they didn’t.

“We do.”

“...?”

“...?”

They did.

* * *

The People's Republic of China.

As its official name suggested, the grand people of this vast continent still embraced socialism as their national ideology.

About twenty years ago, the chairman of the time—who had solidified the foundations of a dictatorship by securing lifelong rule—died during the Great Cataclysm, and power was transferred to a much more moderate regime.

But the core of the system remained unchanged.

- What was the dead chairman’s name again? Pingping? Pengpeng?

Team Leader Choi, who had been responding to Wei Penghu, silently moved his lips. His composure was astonishing.

- …I’m only saying this in case you didn’t know, but you’ll be in serious trouble if you bring up something like that here.

- That’s why I’m using Sound Transmission—or rather, message magic.

- I’m telling you to be careful. Among the outstanding mages of A-rank and above, there are people who can eavesdrop on message magic.

- Anyway, what was his name? Pingping or Pengpeng? I won’t be able to sleep tonight if I don’t find out.

- …Pingping.

*He was going to answer anyway. Why make such a fuss?*

Finally relieved, I listened to Wei Penghu’s words.

“No one could have anticipated it.”

Sichuan Province was a massive province with a vast area and a population of tens of millions.

And all of this had begun in Gaoping District, Nanchong City—one of the more than twenty administrative districts in Sichuan Province.

“As you know, our country has more than ten times as many Gates as other nations. Because of that, we were one of the countries hit hardest during the Great Cataclysm, and we have managed them with corresponding rigor ever since.”

But humans could not control even natural disasters, and the monster wave was a calamity worse than any natural disaster.

“Exactly thirteen minutes after the first sign appeared, we received word that the mana levels in Gaoping District had skyrocketed. And by the time Lei Fei, commander of the Public Security Armed Forces stationed in Sichuan Province, arrived at the scene with the Hunters under his command… everything was already too late.”

“Lei Fei?”

An unfamiliar name. And yet, for some reason, a memory suddenly surfaced.

*The video Team Leader Choi showed me at the Guild house before we left.*

It was still vivid: the city plunged into chaos beneath the hologram’s light, and a man at the head of the Hunters, cutting down monsters one after another.

An aura so brilliant it hurt the eyes had gathered around his weapon.

“I think I’ve seen him before. Is he the man who appeared in the video you sent us…?”

“That’s right.”

Wei Penghu hesitated briefly before continuing with a faint sigh.

“He was one of the S-rank Hunters possessed by our country. Of course, the two of you would not have known that.”

*We wouldn’t have known?*

There were only twenty S-rank Hunters in the entire world. They were absolute powerhouses.

The fame and status they enjoyed were far greater and more formidable than those of even a Supreme Peak master in the Murim.

The internet, the news, and social media were their platforms, while microphones and cameras followed them like shadows.

If ordinary people looked at martial artists with half wariness and half curiosity, modern people looked at Hunters with nothing but admiration.

They were celebrities known throughout the world.

*But we didn’t know about an S-rank Hunter like that?*

Wei Penghu had spoken indirectly, but I understood the meaning behind his words well enough.

Team Leader Choi and I met eyes in midair. At that moment, we were thinking the same thing.

*An undisclosed S-rank Hunter.*

No. More precisely, an S-rank Hunter deliberately concealed by the Chinese government.

*I’d only heard about things like that in rumors. So it was true?*

An S-rank Hunter was practically the face of a nation.

But unlike the weak, who struggled desperately not to be looked down on, the strong hid their claws.

China was already known to possess two S-rank Hunters. Clearly, it had not wanted to reveal all its strength.

Perhaps the world’s other great powers were the same.

*What a thing. Even after going through the Great Cataclysm, they’re still playing this game of one-upmanship.*

It was pathetic. At the same time, I could almost understand it.

Diplomacy. Politics.

I felt as though I had caught a glimpse of the truth of a world I had never understood, and the feeling was strange.

Unlike me, however, Team Leader Choi was much sharper.

“When you say that Lei Fei ‘was’ one of the S-rank Hunters your country possessed, that sounds like the past tense.”

Wei Penghu answered with a grim expression.

“…A week ago, when the first monster wave occurred, Lei Fei disappeared. Along with the Hunters from the Public Security Armed Forces under his command.”

“Are you certain he disappeared? Could it be that…”

“We have not confirmed his death. After that video, the monster called the Lich—no, the Arch Lich—used mana to cut off all communications and surveillance.”

Team Leader Choi and I groaned at the same time.

Hearing our reaction, Wei Penghu asked in a hoarse voice,

“Do you two also think Lei Fei is dead?”

“Hmm.”

“Uh…”

*If someone disappeared in that chaos a week ago, the ending was practically a foregone conclusion.*

At Team Leader Choi’s signal, I cautiously opened my mouth.

“Well, you never know how things will turn out, but…”

“Other experts said he was one hundred percent dead. Useless blowhards, every last one of them.”

*What’s wrong with you? They sound like real experts.*

If anyone claimed he was alive under those circumstances, they should be fired immediately.

That was simply a fact.

“But I think differently. Lei Fei—that boy must still be alive.”

“I hope so too, but realistically speaking…”

“He is my only nephew. My sister, who had been sickly since childhood, died in childbirth. I raised that tiny, unweaned infant as if he were my own son.”

“What?”

*A nephew? You raised him as your own son? What the hell is this?*

As I froze like a statue, Wei Penghu looked at me with tear-filled eyes.

“But what were you going to say? When you said, ‘Realistically speaking,’ I mean.”

*Fuck. This is a crisis of unprecedented proportions.*

My words caught in my throat. I barely managed to squeeze out a voice.

“Well, realistically speaking, I was going to say that there’s still a chance he might be alive.”

“Is that so? Is that true?”

“Yes. But that chance is extremely slim…”

“Thank you, Teacher Jin!”

“No, General. Commander. Great Leader. Just hold on a second and let me finish—”

Grab!

It was too late. Wei Penghu was no longer listening to me.

Instead, he clasped my hand in both of his, his eyes brimming with tears.

“May I ask you for one favor?”

*I wish he wouldn’t.*

Contrary to my desperate hopes, a few seconds later, the words I had been dreading pierced my heart.

“If you happen to meet that boy someday, would you bring him to me?”

“…”

“I beg you.”

Over his desperately pleading shoulders, I saw Team Leader Choi shaking his head.

*What if I had just answered him firmly from the beginning?*

I regretted it, but it was already too late.

In the end, there was only one answer I could give.

“I will. But…”

“Teacher Jin.”

“Yes?”

“You don’t have to say it. I’m already prepared for that.”

“...!”

Wei Penghu wiped the corners of his eyes with his sleeve.

He was no longer a middle-aged man worrying about the safety of his blood relative. He had returned to being the Minister of Defense at the Central Military Commission.

“This is enough. No one was willing to step forward, but you promised me. I can rest easy now.”

“I can’t guarantee anything.”

“What I needed was not someone’s bombastic guarantee. It was a thread of hope.”

Just as Wei Penghu murmured those words, the aircraft descended with a weightless sensation and glided toward the ground.

Outside the window, amid the darkness, I could see rugged mountain terrain, lights moving ceaselessly, and military vehicles.

“It looks like we’ve arrived.”

I had been staring fixedly out the window as though possessed by something. Now I asked,

“Where are we?”

“The temporary operations headquarters.”

“No. That’s not what I asked.”

“Hmm?”

“The mountain. That mountain feels strangely familiar.”

“That’s impossible. As far as I know, you have never entered our country before… Ah, perhaps you saw it in a photograph?”

“A photograph?”

“It is a UNESCO-designated World Cultural Heritage Site, so that would certainly be possible.”

With a faint smile, Wei Penghu continued,

“This is where we established our temporary operations headquarters. Welcome to Mount Qingcheng.”

[^1]: *Sundae-guk* is a Korean soup made with sundae, a type of Korean blood sausage, and is commonly served with rice.
```
