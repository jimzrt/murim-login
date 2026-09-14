<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0382.txt",
      "sha256": "2fb57203aacaf6aa9b38c97ca4c4be1c4753961e2f625105113a0493d2350bca",
      "bytes": 14343
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8314336d3c253270f6880ccfa10c145be9f89ab6a73073cf4ccbb1d7ef9d322f",
      "bytes": 11922
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e042e3a09e4d31d6a1c040ac370542681a4fade7a627fb95c5c73e9497529eb",
      "bytes": 9295
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5466b78c4810bf261bbfd3ef1da0fad15287c720b44f16a8d4386a27dc7eab5d",
      "bytes": 23777
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d0671dc11cbfd469d96fc201c1b610b0979ef98b468d79258c1bfeb687ea102c",
      "bytes": 5293
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 15321
}
-->

# Durable State Update — Chapter 382

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 382. Keep at most
2 continuity_sources. Use only chapter
numbers through 382. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 382,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 382,
    "continuity_sources": [382],
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
    "By the end of the source-only bridge, Jin Taekyung had reached the Supreme Peak realm and Level 120; this chapter grants him another level up, but the resulting level, exact current Fame, Titles, martial-art stages, and unassigned points are not stated.",
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
    "The three beings controlling the undead army are former human necromancers inhabiting dead mage bodies; their individual identities remain unknown.",
    "The Arch Lich is the superior who sent the three beings to kill humans and create more undead. Whether it is the same entity as the Lich previously associated with the monster wave remains unresolved.",
    "Taekyung and Team Leader Choi arrive at the airport aboard the burning private jet. The plane sweeps through roughly half of the monster army and stops near Shao Shen; Choi's barrier magic keeps the occupants alive, though they are unconscious.",
    "Shao Shen recognizes Taekyung as Sibeol-jwa, the Korean Hunter he had seen in the news, and addresses him as Teacher Jin.",
    "The System generates the unexpected Quest Unexpected Assault, with no outcome shown in this chapter.",
    "Taekyung confirms that nearly half of the approximately two-thousand-monster army is undead and that the undead lack life force. He fights them with Scorching Yang Qi, White Flame, Flame Divine Palm, and Flame-Annihilating Divine Fist.",
    "The Skeleton Warlord says the undead are being controlled by someone whose control is weaker than his own and believes the Lich from Taekyung's holographic video probably did not personally participate.",
    "The Skeleton Warlord's chant causes the undead monsters engaged in battle to stop moving, proving that he can influence the army.",
    "The Skeleton Warlord can seize control of nearby undead monsters, make them attack their former allies, and expand the controlled force to roughly two hundred undead.",
    "The Skeleton Warlord's strength is unusually high at Chengdu International Airport because an unexplained surge of mana is flowing through the area.",
    "The three beings have not fully transformed into Liches because one week was insufficient to absorb the death energy required for the transformation.",
    "The three beings combine their power, kill People's Liberation Army soldiers to strengthen the monster army, and deploy or plan to deploy Skeleton Mages, strengthened ogres, Dullahans, and a Death Knight.",
    "Taekyung destroys the undead units sent against him and reaches the three beings before their Death Knight plan can be completed."
  ],
  "continuity_sources": [
    380,
    381
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
    "The individual identities of the three former necromancers controlling the undead remain unresolved.",
    "The outcome of the confrontation between Taekyung and the three beings remains unresolved.",
    "Whether the Skeleton Warlord's expanded control over the undead persists and what effect it will have on the battle remains unresolved.",
    "The outcome of the Unexpected Assault Quest and the ongoing battle at Chengdu International Airport remain unresolved."
  ],
  "safe_through": 381,
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
    "Preserve the pseudo-incantation wordplay for the names of Valencia, Madrid, Bayern Munich, and Stoke City, and for annyeonghaseyo and Yeonye-ga Junggye."
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

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 중화 | **Zhonghua** | Term used in Shao Shen's rallying cry for China. |
| 시벌좌 | **Sibeol-jwa** | Taekyung's profane nickname, recognized by Shao Shen. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 381
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃382화



머리를 치면 몸통은 쓰러지는 법.

우두머리로 보이던 세 놈을 붙잡자 놈들이 통제하고 있던 언데드는 태엽 인형처럼 움직임을 멈췄고, 지휘력을 상실한 몬스터 군단은 뿔뿔이 와해되어 죽거나 도망쳤다.

“아크 리치(Arch Lich)?”

내 물음에 무릎을 꿇고 앉아 있던 세 놈이 고개를 끄덕였다.

이미 죽어서 뼈만 남은 이것들을 ‘놈’이라고 부를 수 있는지는 모르겠지만 어쨌든.

나는 세 개의 두개골을 차례차례 쓰다듬으며 말을 이었다.

“사람이 말을 하면 대답을 해야지. 너희 지금 죽었다고 유세 부리니?”

말이 끝나기가 무섭게 대답이 튀어나왔다.

- 예. 예. 아크 리치가 맞습니다.

- 인간님께서 들으신 것이 정확합니다.

- 그렇다.

“음. 아크 리치라. 처음 들어 보는 몬스터인데…… 그런데 마지막에 반말로 대답한 놈 누구냐.”

- 저놈입니다!

- 감히 위대하신 인간님께!

휙, 휙!

뼈만 남은 손가락들이 한 놈을 가리켰다.

전광석화와도 같은 동료들의 배신에, 지목당한 놈이 두개골을 바르르 떨었다.

- 아니다! 이건 비열한 모함이다!

“……내 생각에는 모함이 아닌 것 같은데.”

거짓말을 할 거면 말투라도 좀 고치든가.

슬쩍 주위를 확인한 나는 인벤토리에서 ‘그것’을 꺼내 들었다.

“골골아. 간식 먹자.”

기묘한 검은 광택이 흐르는 두개골 하나. 그것의 텅 빈 동공에서 불꽃이 일렁인다.

- ……골골이라니. 그럴 바에야 차라리 전처럼 워로드몬이라고 불러라.

“왜, 해골이니까 골골이. 찰떡인데.”

- 본 사령관을 이렇게 모욕하다니!

“뭐 싫으면 말든가.”

다시 인벤토리에 집어넣으려던 그때, 스켈레톤 워로드가 분노한 목소리로 외쳤다.

- 잘 먹겠습니다!

“솔직한 아이로구나.”

솔직한 아이에게는 상을 줘야지. 거짓말이나 치는 나쁜 놈에게는 벌을 주고.

“자, 이제 시식해.”

- 고맙구나. 조금 덜 간악한 인간이여. 그런데 얼마나 먹어야……?

“아까처럼 조금만.”

- 으음. 좀 더 먹고 싶은데. 하지만 알겠다.

간식도 너무 자주 주면 과한 법. 살짝 아쉬움을 표한 스켈레톤 워로드가 벌벌 떨고 있는 놈을 향해 입을 쩍 벌렸다.

- 자, 이리 오너라.

- 히, 히이익! 안 돼!

- 돼!

스켈레톤 워로드의 단호한 외침과 동시에 변화가 시작되었다.

쏴아아악!

저건 다시 봐도 신기하네.

마치 진공청소기로 빨아들이는 것처럼, 무릎을 꿇고 있는 놈의 몸뚱어리에서 흘러나온 검은 안개가 스켈레톤 워로드에게 흡수되기 시작한다.

- 흐어어어억!

변화는 거기에서 끝나지 않았다.

검은 안개, 스켈레톤 워로드가 사기(死氣)라고 부르는 그것이 흘러나올수록 놈의 안색, 아니 뼈다귀가 점점 새하얗게 변해 갔다.

반면 스켈레톤 워로드는 검은 광택이 더욱더 깊고 진해졌다.

- 그, 그만!

- 후후후. 이토록 맛 좋은 사기라니.

- 안 돼애!

- 본 사령관이 전부 가져가 주마. 사기이잇!

빡!

- 흡!

“사기잇 같은 소리 하네. 어디서 이상한 것만 배워서는.”

- ……네가 할 소린가?

“아무튼 이제 그만 먹어라.”

- 어째서!

“살쪄.”

순간 할 말을 잃은 스켈레톤 워로드를 품 안에 집어넣고 놈을 바라봤다.

처음 봤을 때만 해도 거무튀튀하던 뼈다귀는 어느새 반쯤 백골이 된 상태. 상당한 사기를 흡수당한 탓인지, 동공 안의 녹색 불빛이 위태롭게 휘청거린다.

- 크흡, 크흐흑.

뼛속까지 쪽쪽 빨린 동료의 약해진 모습에, 나머지 두 녀석은 초조하게 이빨을 딱딱 부딪쳤다.

- 무엇이든 하문하십시오. 위대하신 화염의 지배자시여.

- 부디 바라옵건대. 이 하찮은 존재, 오르페우스 폰 막시무스 발렌시아 바이엘른의 충성을 받아 주시옵소서.

“……언데드가 아니라 비데인가.”

어지간히 힘을 잃기 싫은 모양이다. 뭐 이렇게 협조적으로 나와주면 나야 고맙긴 하지만.

“자, 아직 말 안 한 게 있으면 밑바닥까지 싹싹 긁어서 털어놔 봐. 만약 거짓부렁을 늘어 놨다가는…….”

- 전부 말하겠습니다!

- 부디 바라옵건대, 이 거짓되고 하찮은 존재가 진실을 말씀드리도록 허락해 주소서!

- 마, 말하겠습니다.

이대로 사골국물이 되기는 싫은지 세 뼈다귀는 열정적으로 질의응답에 참여했다.

일주일 전, 아크 리치의 첫 등장부터 지금까지 벌어진 모든 일 들을 빠짐없이 들은 나는 짐짓 눈살을 찌푸렸다.

“확실해?”

- 그렇사옵니다!

- 죽음의 강에 맹세합니다!

- 하, 한 치의 거짓도 없습니다.

격렬하게 두개골을 끄덕이는 세 놈의 모습에, 스켈레톤 워로드가 불쑥 끼어들었다.

- 사실이다.

“얘네한테 뒷돈 받았냐? 그걸 네가 어떻게 장담해?”

- 죽음의 강에 맹세했으니까. 그건 우리 같은 존재에게는 절대적인 약속이다. 결코 거스를 수 없는.

“흠.”

평소에는 먼지처럼 가볍던 녀석이 저렇게 무게를 잡고 말하는 걸 보면 거짓말은 아닌 것 같다.

사실 지금 같은 상황에 놈들이 수작을 부릴 이유도 없고.

“오케이. 믿어 주지.”

- 감사합니다! 정말 감사합니다!

- 크흐흐흑! 충심을 다하겠나이다. 나의 왕이시여!

- 나, 아니 저도 인간님께 충성하겠습니다. 앞으로는 두 번 다시 오늘과 같은 일을 저지르지 않을 것을 죽음의 강에 맹세…….

콰직!

마지막 놈은 말을 잇지 못하고 머뭇거렸다.

파르르 떨리는 녹색 안광이 자신의 가슴팍에 틀어박힌 주먹과 나를 번갈아 바라본다.

- 어, 어째서?

“어째서긴 뭘 어째서야.”

- 나, 나는, 충성을, 맹세, 죽음의 강…….

“늦었어.”

남의 것처럼 차가운 목소리가 입술을 비집고 흘러나왔다.

“너희가 한 짓을 되돌리기에는.”

바로 오늘, 이 자리에서 수많은 사람이 죽었다.

화기를 갖춘 정규군과 헌터들로도 놈들을 막을 수 없었으니, 지난 일주일 동안 몬스터 군단의 손에 죽은 민간인들은 헤아릴 수조차 없을 것이다.

“충성은 필요 없어. 너희 같은 새끼들이 바치는 거라면 더더욱.”

단전에서 끌어 올린 열양지기를 흘려 보낸 순간.

화륵!

놈의 갈비뼈를 부수고 박혀 있던 주먹에서 극양의 기운이 피어올랐다. 초고온의 열기를 띤 청백색의 강기가 놈의 전신을 휘감았다.

콰아아아!

보였다. 바람 앞의 촛불처럼 휘청이던 놈의 녹색 안광이 꺼지는 광경이.

그리고 튕기듯이 몸을 일으키며 주문을 영창하는 두 놈의 모습도.

- 자즈차와 엄바도……!

- 바르간 마흐라……!

후우웅.

놈들을 중심으로 흩날리는 마력의 바람. 사악한 마법의 주문이 완성되려던 그때, 나는 한마디를 툭 내뱉었다.

“먹어 치워. 전부.”

마치 그 말만을 기다리고 있었다는 듯, 품 안에 넣어 둔 스켈레톤 워로드가 옷자락 사이로 뛰쳐나오며 입을 쩍 벌렸다.

- 얼마든지.

- 바르사바…… 히이익!

- 아, 안 돼!

살고자 하는, 아니 계속 언데드로 남아 있고자 하는 몬스터들의 마지막 단말마.

그러나 놈들의 염원과는 달리 스켈레톤 워로드의 흡입력은 그 어느 때보다 강했고, 신속했다.

쏴아아악! 꿀꺽!

엄청난 양의 사기를 한입에 집어삼킨 스켈레톤 워로드가 두개골을 부르르 떤 다음 순간, 모든 기운을 빼앗긴 두 개의 해골이 와르르 허물어졌다.

띠링. 띠링. 띠링.



- 돌발 퀘스트, [예상치 못한 습격]을 성공적으로 완료했습니다!

- 당신은 몬스터 군단을 와해시켰습니다! 이는 실로 뛰어난 업적입니다!

- 퀘스트 보상으로 칭호, [언데드 헌터]를 획득했습니다!

- 상당량의 경험치와 명성을 획득했습니다!

- 레벨 업!



고작 한 번?

예전 같았으면 레벨 업 몇 번은 거뜬했을 텐데, 120레벨이 되고 나니 필요한 경험치가 많아진 모양이다.

‘경험치 얻자고 한 일은 아니긴 한데.’

마땅히 해야 할 일을 했을 뿐이지만, 약간의 아쉬움이 드는 건 어쩔 수 없다.

강해지면 강해질수록, 앞으로의 전투에 더 큰 도움이 될 테니까.

‘저놈도 마찬가지고.’

나는 내심 중얼거리며 스켈레톤 워로드를 바라봤다.

엄청난 양의 사기를 흡수한 덕분인지, 녀석에게서 느껴지는 힘은 처음 만났던 그때와 비교할 바가 아니었다.

- 으음. 후우우우…….

두개골에 뚫린 코와 귀, 눈 등의 구멍 사이로 검은 안개가 뭉게뭉게 피어오른다.

횃불처럼 타오르는 보랏빛 안광과 매끈한 묵광을 자랑하는 표면. 이내 내 머릿속에 녀석의 광소가 쩌렁쩌렁 울려 퍼졌다.

- 크하, 크하하하하!

“볼륨 좀 줄여라. 시끄럽다.”

- 너, 간악한 인간이여. 이번만큼은 본 사령관이 네게 큰 감사를 표하마.

“당연히 그래야지. 누가 먹이를 줬는데.”

내 시큰둥한 대답에 스켈레톤 워로드가 발끈했다.

- 먹이라니! 이 몸이 애완동물이라도 된다는 건가!

“비슷하지. 아냐?”

- 헛소리하지 마라!

“그래? 골골이, 돌아와.”

내가 손을 내밀자 튕기듯 폴짝 뛰어올라 손바닥 위에 안착하는 두개골.

나는 상으로 녀석의 미간을 살살 긁어 주었다.

“잘했어, 골골이. 어유 예뻐.”

- ……!

두개골이 부들부들 떨렸다.

- 이, 이럴 수가! 본 사령관이 어찌 인간 따위에게!

“입은 아니라고 하지만, 몸은 솔직한 거지.”

- 나는 검은 숲의 주인이자, 위대한 언데드 군단의 사령관이다. 이 몸을 능멸하지 말라!

“머리통만 남은 사령관?”

- 뭣이! 이깟 신체 따위. 사기를 소모한다면 얼마든지 복구할 수 있다!

“그래? 그런데 왜 지금까지 복구 안 했어?”

- ……복구해 봤자 어차피 웬 미친 인간이 박살 낼 테니까.

“오, 정답.”

까드득. 이빨도 없어서 뼈마디를 간 스켈레톤 워로드의 안광이 가늘어졌다.

- 어째서냐, 간악한 인간.

“뭐가?”

- 내게 먹이를, 아니 이토록 큰 힘을 준 꿍꿍이가 있을 것 아닌가. 시커먼 속내가 있는 것이 분명할 터. 진실을 고하라!

잠깐 생각하던 나는 대답했다.

“음. 네가 좆밥이라서.”

- 어?

“어차피 넌 나 못 이겨. 그럴 거면 좀 더 강하고 쓸모있는 좆밥을 데리고 다니는 게 써먹기도 편하잖아. 안 그래?”

- ……!

“자, 이제 안에 들어가 있어라. 사람들 온다.”

나는 충격으로 굳어 버린 녀석을 인벤토리에 집어넣고 자리에서 일어났다.

본래는 공항 직원과 승객들로 붐볐을 공항 면세점 복도. 텅 비고 어두컴컴한 그곳에서 이쪽을 향해 걸어오는 세 사람이 있었다.

그리고 그중 두 사람은 낯익은 얼굴이었다.

“진태경 씨.”

「진 선생님.」

비교적 멀끔한 상태인 최 팀장과 중국 공안 무력부 소속의 A급 헌터인 샤오 쉔이다.

전투가 끝난 지 상당한 시간이 흘렀음에도 여전히 피와 먼지를 뒤집어쓴 채인 샤오 쉔의 얼굴은 피곤에 찌들어 있었다.

「여기 계셨군요.」

나는 최 팀장을 향해 눈인사를 건네며 둘러댔다.

“네. 잠시 할 일이 있어서요.”

「말씀 낮춰 주십시오. 시벌, 아니 진 선생님께서는 저와 제 동지들. 나아가 중화의 인민을 구한 영웅이십니다.」

“…….”

착각인가. 저놈 방금 시벌좌라고 하려고 했던 것 같은데.

내 생각을 아는지 모르는지, 샤오 쉔은 지극히 공손한 태도로 말을 이었다.

「다행히 평화 길드에서 오신 두 선생님의 도움으로 몬스터들을 격퇴할 수 있었습니다. 이 자리를 빌려 다시 한번 감사를 표합니다.」

“아, 예. 뭘 이 정도 가지고. 마땅히 해야 할 일이었는데요.”

나는 손사래를 치며 힐끗 최 팀장의 눈치를 살폈다.

혹시나 [통합 언어팩]이 잘못 작동해서 이상함을 눈치채면 어쩌나 했는데, 지금은 대화를 나누는 상대가 샤오 쉔인 만큼 내가 하는 말도 최 팀장의 귀에는 중국어로 들리는 것 같았다.

“그런데 옆에 계신 분은……?”

이들 중 유일하게 낯선 사람.

묵묵히 우리의 대화를 듣고 있던 반백의 장년인이 손을 내밀어 악수를 청했다.

「중앙 군사위원회에서 국방부장을 맡고 있는 웨이펑후라고 하오. 반갑소, 진 선생.」

“국방부장이라면…….”

「계급은 상장이오.」

“아아.”

대단한 사람인 건 알겠는데, 상장이 뭔진 모르겠다.

내 생각을 읽었는지, 옆에서 최 팀장이 개미만 한 목소리로 속삭였다.

“포 스타요. 포 스타.”

“아아, 아아아! 대장님이셨구나! 만나서 반갑습니다!”

나도 한때 별이 네 개였다. 어릴 때 했던 그 게임 참 재밌었지. 차기작은 쪽박도 그런 쪽박이 없었지만.

내 반응에 장년인, 웨이펑후가 희미한 미소를 띠며 손을 맞잡았다.

「젊은 분이라 그런지, 혈기왕성하시구려. 진 선생께 물어볼 것이 많은데…… 우선 가면서 얘기하시겠소?」

“그러죠, 뭐.”

웨이펑후를 따라 발걸음을 옮기려던 내가 멈칫했다.

“그런데 어디로 갑니까?”

「작전 본부요. 제트기를 대기시켜 두었소.」

“예? 본부? 제트기요?”

「그렇소. 모두 그곳에서 진 선생을 기다리고 있지.」

모두라니. 누구?
```

## Final English reading copy

```markdown
# Chapter 382

Strike the head, and the body falls.

Once I got hold of the three who looked like leaders, the undead they had been controlling stopped moving like clockwork dolls. The monster army, deprived of its command, scattered and collapsed, with some dying and others fleeing.

“Arch Lich?”

At my question, the three creatures sitting on their knees nodded.

I wasn’t sure whether I could still call things that had already died and been reduced to bones “creatures,” but whatever.

I stroked each of the three skulls in turn and continued.

“When someone speaks to you, you’re supposed to answer. Are you throwing your weight around just because you’re dead?”

The answer came flying out before I had even finished speaking.

- Yes. Yes. It is indeed the Arch Lich.

- What the great human heard is accurate.

- That is so.

“Hmm. Arch Liches. That’s a monster I’ve never heard of before… But which one of you just answered me informally?”

- That one!

- How dare he speak to the great human like that!

Whoosh! Whoosh!

The skeletal fingers pointed at one of them.

Betrayed by his comrades with lightning speed, the accused skull began to tremble.

- No! This is a vile slander!

“…I don’t think it’s slander.”

If you’re going to lie, at least put on a respectful tone.

I casually checked my surroundings, then pulled *it* out of my inventory.

“Boney. Time for a snack.”

A skull with a strange black sheen. Flames flickered inside its empty eye sockets.

- …Boney? You might as well call me Warlordmon like before.

“Why? You’re a skeleton, so Boney. Perfect fit.”

- To think you would insult this commander like this!

“What? If you don’t like it, forget it.”

I was about to put him back in my inventory when the Skeleton Warlord shouted furiously.

- I will gladly eat it!

“You’re an honest little thing.”

An honest little thing deserved a reward. A bad one that lied deserved punishment.

“Here. Try it.”

- Thank you. You are a slightly less wicked human. But how much should I eat…?

“Just a little, like before.”

- Hmm. I want to eat more. But I understand.

Too many snacks would be overdoing it. Showing a hint of disappointment, the Skeleton Warlord opened his mouth wide at the trembling creature.

- Come here.

- Eek! No!

- Yes!

The change began with the Skeleton Warlord’s firm declaration.

Whoooooosh!

That was still amazing, no matter how many times I saw it.

Like something being sucked up by a vacuum cleaner, black mist began flowing out of the kneeling creature’s body and being absorbed by the Skeleton Warlord.

- Gaaaaaah!

The change didn’t end there.

The black mist—the substance the Skeleton Warlord called death energy—continued to flow out. The creature’s complexion, or rather its bones, gradually turned whiter and whiter.

Meanwhile, the Skeleton Warlord’s black sheen grew deeper and darker.

- S-Stop!

- Hehehe. Such delicious death energy.

- Noooo!

- This commander shall take it all. Death energyyyy!

Crack!

- Hk!

“Don’t go saying things like ‘death energyyyy.’ Where did you even learn that weird crap?”

- …Is that really something you can say?

“Anyway, stop eating now.”

- Why?!

“You’ll get fat.”

The Skeleton Warlord fell silent for a moment. I tucked him against my chest and looked at the creature.

When I had first seen it, its bones had been dark and grimy. Now, it was halfway to becoming a bleached skeleton. Perhaps because it had lost so much death energy, the green light in its eye sockets wavered dangerously.

- Sob… sob…

At the weakened state of their comrade, who had been drained to the bone, the other two creatures anxiously clacked their teeth together.

- Ask anything of us, great ruler of flame.

- I humbly beseech you. Please accept the loyalty of this lowly being, Orpheus von Maximus Valencia Bayern.

“…Are you undead, or are you bidets?”

They really didn’t want to lose their strength. I appreciated their cooperation, though.

“All right. If there’s anything you haven’t told me, scrape the bottom clean and spill every last detail. But if you start spewing lies…”

- We will tell you everything!

- I humbly beseech you. Please permit this false and lowly being to speak the truth!

- W-We will tell you.

Perhaps they didn’t want to become bone broth. The three skeletons participated enthusiastically in the interrogation.

After hearing every detail of what had happened over the past week, from the Arch Lich’s first appearance until now, I deliberately furrowed my brow.

“Are you sure?”

- Yes, we are!

- We swear upon the River of Death!

- Th-There is not a single lie.

As the three creatures vigorously nodded their skulls, the Skeleton Warlord suddenly interrupted.

- It is true.

“Did they pay you off? How can you guarantee that?”

- Because they swore upon the River of Death. It is an absolute promise to beings like us. One that can never be broken.

“Hmm.”

The Skeleton Warlord was usually as light as dust, so the fact that he was speaking with such gravity made me think he wasn’t lying.

Besides, there was no reason for them to scheme in a situation like this.

“Okay. I’ll believe you.”

- Thank you! Thank you so much!

- Sob, sob! I shall devote my entire heart to your service, my king!

- I-I will serve the human, too. I swear upon the River of Death that I will never again commit an act like today’s—

Crack!

The last creature couldn’t finish speaking and faltered. The trembling green light in its eyes shifted between the fist buried in its chest and me.

- Wh-Why?

“Why do you think?”

- I-I will swear my loyalty. I swear upon the River of Death—

“Too late.”

A voice so cold it seemed to belong to someone else slipped through my lips.

“You can’t undo what you did.”

A great many people had died here, today.

Even regular troops equipped with firearms and Hunters had been unable to stop them. There was no way to count all the civilians who had died at the hands of the monster army over the past week.

“I don’t need your loyalty. Especially not from pieces of shit like you.”

The moment I released the Scorching Yang Qi I had drawn up from my dantian—

Fwoosh!

Extreme Yang qi surged from the fist embedded in the creature’s shattered ribs. Blue-white sword qi, carrying ultra-high heat, coiled around its entire body.

Kaaaa-boom!

I saw it.

The green light in its eyes, wavering like a candle in the wind, went out.

I also saw the other two creatures spring to their feet and begin chanting spells.

- Jajeuchawa Eumbado…!

- Bareugan Mahra…!

Whoooong.

A magical wind swirled around them. Just as the evil spell was about to be completed, I casually spoke one word.

“Devour them. All of them.”

As though it had been waiting for those words, the Skeleton Warlord leaped out from among my clothes and opened its mouth wide.

- Gladly.

- Barsaba… Eeeek!

- N-No!

The monsters’ final cries were filled with the desire to live—or rather, the desire to remain undead.

But contrary to their wishes, the Skeleton Warlord’s suction was stronger and faster than ever.

Whoooooosh! Gulp!

After swallowing an enormous amount of death energy in one bite, the Skeleton Warlord’s skull trembled.

The next moment, the two skeletons, drained of every last trace of energy, crumbled to the ground.

Ding. Ding. Ding.

> **System**
>
> - The unexpected Quest, **Unexpected Assault**, has been successfully completed!
>
> - You have routed the monster army! This is truly an outstanding achievement!
>
> - As a Quest Reward, you have acquired the Title **Undead Hunter**!
>
> - You have acquired a considerable amount of EXP and Fame!
>
> - Level Up!

Only once?

In the past, I would have leveled up several times without a problem. But now that I had reached Level 120, it seemed the EXP requirement had increased.

*It’s not like I did this for the EXP.*

I had only done what needed to be done, but I couldn’t help feeling a little disappointed.

The stronger I became, the more useful I would be in future battles.

*That one is the same.*

I looked at the Skeleton Warlord.

Perhaps because he had absorbed such a massive amount of death energy, the power I felt from him was incomparable to what I had sensed when we first met.

- Hmm. Hoooooo…

Black mist billowed from the holes in his skull where his nose, ears, eyes, and other features should have been.

Purple light blazed in his eyes like torches, and the surface of his skull gleamed with a smooth, dark luster. Then his booming laughter echoed through my head.

- Krah, hahahahaha!

“Turn down the volume. You’re loud.”

- You vile human. This time, this commander shall express his great gratitude to you.

“You should. Who was it that fed you?”

At my indifferent reply, the Skeleton Warlord flared up.

- Food?! Are you saying this body has become a pet?!

“Something like that. Isn’t it?”

- Do not spout nonsense!

“Really? Boney, come back.”

I held out my hand.

The skull leaped up as though spring-loaded and landed neatly on my palm.

As a reward, I gently scratched the spot between his eyes.

“Good job, Boney. Who’s a pretty boy?”

- …!

The skull trembled violently.

- H-How can this be?! How can this commander possibly… to a mere human?!

“Your mouth says no, but your body is honest.”

- I am the master of the Black Forest and commander of the great undead legion. Do not humiliate this body!

“A commander with only a head left?”

- What?! This paltry body is nothing! If I expend death energy, I can restore it as many times as I wish!

“Really? Then why haven’t you restored it yet?”

- …Because some crazy human would just smash it again anyway.

“Oh, correct.”

Grind.

The Skeleton Warlord had no teeth, so he ground his bones together instead. His eye sockets narrowed.

- Why, you vile human?

“What?”

- You must have an ulterior motive for giving me food—or rather, granting me such great power. You clearly have some sinister intention. Tell me the truth!

I thought for a moment before answering.

“Hmm. Because you’re a fucking weakling.”

- Huh?

“You can’t beat me anyway. If I’m going to drag you around, it’s easier to make use of a stronger, more useful fucking weakling, isn’t it?”

- …!

“Now get back inside. People are coming.”

I put the creature, frozen with shock, back into my inventory and stood up.

The airport duty-free corridor would normally have been packed with airport employees and passengers. Now, three people were walking toward me through the empty, gloomy passage.

Two of them were familiar faces.

“Mr. Jin Taekyung.”

“Teacher Jin.”

They were Team Leader Choi, who was in relatively decent condition, and Shao Shen, an A-rank Hunter belonging to the Public Security Armed Forces of China.

A considerable amount of time had passed since the battle ended, but Shao Shen’s face was still covered in blood and dust, and exhaustion had sunk deep into his features.

“So you were here.”

I greeted Team Leader Choi with a glance and made an excuse.

“Yes. I had something to take care of.”

“Please speak casually. Sibeol—no, Teacher Jin, you are a hero who saved me and my comrades. More than that, you saved the people of Zhonghua.”

“……”

Was it my imagination, or had he just been about to call me Sibeol-jwa?

Whether he knew what I was thinking or not, Shao Shen continued in an extremely polite tone.

“Fortunately, with the help of the two gentlemen from Peace Guild, we were able to repel the monsters. I would like to take this opportunity to thank you once again.”

“Ah, yes. It was nothing. It was simply what needed to be done.”

I waved my hands modestly, then glanced at Team Leader Choi.

I had been worried that the Integrated Language Pack might malfunction and he would notice something strange. But since Shao Shen was the person I was speaking with, it seemed that even my words sounded like Chinese to Team Leader Choi.

“But who is the gentleman beside you…?”

The only unfamiliar person among them was a middle-aged man with half-gray hair.

He had been listening silently to our conversation. Now he extended a hand for a handshake.

“I am Wei Penghu, the Minister of Defense at the Central Military Commission. It is a pleasure to meet you, Teacher Jin.”

“The Minister of Defense…?”

“My rank is Senior General.”

“Oh.”

I understood that he was an important person, but I had no idea what a Senior General was.

Perhaps he read my thoughts, because Team Leader Choi whispered from beside me in a voice as tiny as an ant.

“Four-star. Four-star.”

“Oh, ohhh! So you’re a four-star general! Nice to meet you!”

I had been a four-star once, too. The game I played as a kid had been a lot of fun. The sequel had flopped so hard it was practically in a league of its own.

At my reaction, Wei Penghu gave a faint smile and clasped my hand.

“Perhaps because you are young, you are full of youthful vigor. I have much to ask Teacher Jin, but… shall we talk while we make our way there?”

“Sure, why not?”

I started following Wei Penghu, then stopped.

“But where are we going?”

“To the operations headquarters. I have a jet standing by.”

“What? Headquarters? A jet?”

“That is correct. Everyone is waiting for Teacher Jin there.”

Everyone?

Who?
```
