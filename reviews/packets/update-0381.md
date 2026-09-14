<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0381.txt",
      "sha256": "72b34dc3a00ee4cf069f91194c3af311d1130c076cc35a6d9f69dc13f13df4a1",
      "bytes": 15670
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7c28c431ddc5e057db0504385bc50911460d0896ee5547d25714c46c63864f72",
      "bytes": 10141
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b0fc062b5fd5d4721e3910b74b79a1a115793958cba844cb91930ea7eff07915",
      "bytes": 8893
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "908bcb8aa7ffe983fe02a8c17b32268debb3ceb0a0217e90bb7877c5d23a4bcb",
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
  "estimated_tokens": 15327
}
-->

# Durable State Update — Chapter 381

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 381. Keep at most
2 continuity_sources. Use only chapter
numbers through 381. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 381,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 381,
    "continuity_sources": [381],
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
    "The identity of the beings controlling the undead army is not established.",
    "Taekyung and Team Leader Choi arrive at the airport aboard the burning private jet. The plane sweeps through roughly half of the monster army and stops near Shao Shen; Choi's barrier magic keeps the occupants alive, though they are unconscious.",
    "Shao Shen recognizes Taekyung as Sibeol-jwa, the Korean Hunter he had seen in the news, and addresses him as Teacher Jin.",
    "The System generates the unexpected Quest Unexpected Assault, with no outcome shown in this chapter.",
    "Taekyung confirms that nearly half of the approximately two-thousand-monster army is undead and that the undead lack life force. He fights them with Scorching Yang Qi, White Flame, Flame Divine Palm, and Flame-Annihilating Divine Fist.",
    "The Skeleton Warlord says the undead are being controlled by someone whose control is weaker than his own and believes the Lich from Taekyung's holographic video probably did not personally participate.",
    "The Skeleton Warlord's chant causes the undead monsters engaged in battle to stop moving, proving that he can influence the army."
  ],
  "continuity_sources": [
    380
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
    "The identity of the beings controlling the undead army remains unresolved.",
    "Whether the Skeleton Warlord's control over the undead persists and what effect it will have on the battle remains unresolved.",
    "The outcome of the Unexpected Assault Quest and the ongoing battle at Chengdu International Airport remain unresolved."
  ],
  "safe_through": 380,
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
    "Render 시벌좌 as Sibeol-jwa, 중앙 군사 위원회 as Central Military Commission, 화염신장 as Flame Divine Palm, and 멸염신권 as Flame-Annihilating Divine Fist."
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
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 리치 | **Lich** | Supreme undead monster associated with the recent monster wave. |
| 듀라한 | **Dullahan** | Higher undead monster form taken by Yao Wei. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 380
- **Aliases:** Sleeping Dragon of Shanxi; Huashan Divine Dragon; Blazing Fire Divine Dragon
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; Supreme Peak martial artist; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃381화



솨아아아.

보이지 않는다. 그러나 느껴진다. 나를 중심으로, 아니 인벤토리라는 아공간에 존재하는 스켈레톤 워로드로부터 흘러나온 끈적한 기운이 사방으로 뻗어 나가는 것이.

변화는 순식간에 일어났다.

- 키릭?

- 구워?

흉포하기 그지없던 몬스터들의 움직임이 우뚝 멈췄다.

오크, 트롤, 고블린, 라이칸스로프와 몬스터 백과사전에서나 보던 온갖 종류의 몬스터와 전사한 헌터들까지.

놈들의 공통점은 단 하나, 이미 한 번 죽어 언데드로 부활했다는 점이었다.

꿀꺽.

마른침을 삼킨 내가 중얼거렸다.

“이게 되네.”

- 와, 이게 진짜 되네.

“……?”

- ……?

아니, 지금 뭐라고?

순간 뇌정지가 온 나는 작게 속삭였다.

“무슨 개뼈다귀 같은 소리야. 당연히 되니까 한 거 아니었어?”

스켈레톤 워로드가 우물쭈물 대답했다.

- 그게 사실…… 본 사령관도 이렇게 쉽게 될 줄 몰랐다.

“네 통제력이 훨씬 높다면서?”

- 아, 그건 홧김에 그냥 해 본 말인데.

“뭐?”

- 가만히 있기에는 자존심이 상해서…….

“…….”

이거 완전 미친놈 아냐.

어이가 없었지만, 그것과는 별개로 결과는 확실했다.

반경 수십 미터에 존재하던 언데드 몬스터들이 일시에 움직임을 멈추자 주위에서 벌어지던 치열한 전투도 잠시 소강상태에 빠진 것이다.

「모, 몬스터들이 움직임을 멈췄다!」

「이게 도대체 무슨 상황이지?」

「방심하지마! 아직 움직이는 놈들이 있다!」

누군가의 외침대로, 방심하기에는 아직 일렀다.

스켈레톤 워로드의 통제에 들어온 것은 근처의 일부 언데드 몬스터일 뿐, 멀리 떨어져 있거나 언데드 상태가 아닌 일반 몬스터의 경우는 예외였으니까.

- 우워어어어!

- 취이익!

“흐아아압!”

카가가강! 푸푹!

갑작스러운 동족의 변화에 어리둥절하던 것도 잠시, 통제가 되지 않는 몬스터들이 재차 날뛰기 시작하자 다시금 전투가 시작되었다.

머릿수에서부터 비교가 되지 않는 싸움. 그러나 지금 이 순간부터는 달라질 것이다.

나는 한껏 숨죽인 목소리로 외쳤다.

“가라, 워로드몬!”

발끈한 워로드몬, 아니 스켈레톤 워로드가 외쳤다.

- 간악한 인간이여! 본 사령관을 그렇게 부르지 말라!

“그럼 소멸하고 싶어서 환장한 워로드몬?”

- ……빌어먹을.

숨도 못 쉬는 해골 주제에 한숨을 푹 내쉬더니 이내 마법의 주문을 외운다.

- 싸워라, 해골해골.

저놈도 해골해골에 재미가 들린 게 틀림없다. 별 우습지도 않은 주문이었지만 효과는 확실했다.

- 구워?

스켈레톤 워로드의 명령에, 멍하니 풀려 있던 언데드 몬스터들의 눈동자에 흉포함이 서린다. 그리고 다음 순간.

콰직!

언데드 오우거의 쇠몽둥이가 어느 트롤의 머리통을 부수는 것을 시작으로, 새로운 주인을 섬기게 된 언데드 몬스터들이 동족을 향해 달려들었다.

- 쿠워어어어!

- 취, 취릭?

빠각! 서걱! 푸푸푹!

등 뒤에서 벌어진 예상치 못한 아군의 기습. 중국 헌터들을 포위하고 있던 몬스터 군단의 한 축이 속절없이 허물어졌다.

- 취이이익!

「뭐, 뭐야!」

「갑자기 저놈들이 왜……?」

당황한 것은 동족에게 배신당한 몬스터들 뿐만이 아니었다.

갑작스러운 상황에 얼떨떨해하는 중국 헌터들. 나는 그들의 선두에서 줄곧 종횡무진 창을 휘두르던 청년 헌터를 향해 외쳤다.

“샤오 쉔!”

「지, 진 선생님?」

동그래진 눈동자가 나를 바라봤다.

「어, 어떻게 제 이름을?」

방금 [기감]으로 레벨 창을 확인해서 알게 된 거지만, 지금은 그게 중요한 게 아니다.

“뭐 합니까! 적극 공세로 전환하지 않고.”

「그런데 이 상황은 도대체…….」

“지금 그게 그렇게 궁금해요? 언데드 몬스터 하나 붙잡고 육하원칙에 따라 왜 우리를 돕는지 설명을 듣고 싶어?”

「아, 아닙니다!」

“그럼 이제 어떻게 해야 될까?”

정신이 번쩍 든 샤오 쉔이 창을 번쩍 치켜들었다.

「공격 대형! 공안 무력부 전원, 지금부터 언데드 몬스터들을 제외한 나머지를 친다!」

「옛!」

훌륭한 판단의 표본이로군.

하나가 된 외침과 함께 궁지에 몰려 있던 오백여 명의 헌터들의 기세가 바뀌었다.

「죽여!」

「동지들의 원한를 갚아라!」

쉬쉬쉬쉭, 서걱!

- 아우우우!

막 오크의 목을 잘라낸 헌터를 향해 달려드는 라이칸스로프.

누런 송곳니로 목줄기를 물어뜯으려는 놈의 아가리를 거대한 주먹이 후려쳤다.

콰직!

- 그워어어어!

라이칸스로프의 두개골을 박살 낸 오우거가 흉포한 함성을 내질렀다. 그런 오우거의 머리 위로 급강하한 그리폰의 날카로운 발톱이 번쩍 빛을 발했다.

- 끼이이이익!

날카로운 괴성. A급 몬스터의 마력이 실린 발톱이 오우거의 안구를 할퀴려던 그 순간.

「아이스 볼!」

「라이트닝 볼트!」

대기하고 있던 원거리 헌터들의 마법에, 감전된 그리폰이 허공에서 몸을 부르르 떨었다.

바로 그때, 트롤의 어깨를 밟고 솟구친 한 인영이 그리폰을 향해 무기를 휘둘렀다.

“독일 최고의 무기 공방으로 손꼽히는 J사에서 특별 제작한……!”

서걱!

군더더기 없이 깔끔한 일격이 그리폰의 머리를 가른다.

우아하게 착지한 최 팀장이 피 한 방울 묻지 않은 투명한 검신을 바라보며 흡족하게 웃었다.

“경매가 52억에 낙찰받은 롱소드. 역시 제값을 하는군.”

“…….”

병신 같은데 멋있어. 멋있긴 한데 병신 같아.

그 광경을 지켜보던 스켈레톤 워로드가 떨떠름한 목소리로 물었다.

- 간악한 인간이여, 저 인간이 네 상관이라고 했나?

“아니, 그. 길드 내부 직책상으로 따지면 그렇긴 한데…….”

- 인간치고는 제법 똑똑해 보였는데, 별 괴상한 인간을 다 보겠군. 과연 네 녀석의 상관답다.

“혓바닥 잘못 놀려서 소멸하고 싶은 스켈레톤 워로드 손?”

짧게 침묵한 스켈레톤 워로드는 주문을 외는 것으로 대답을 대신했다.

- 자라나라, 해골해골!

서당 개 삼 년이면 풍월을 읊는다고, 이제는 시키지 않아도 알아서 잘한다.

투둑, 투두두둑.

최 팀장에게 죽은 그리폰이, 헌터와 언데드의 합공에 의해 쓰러진 몬스터들이 새로운 생명을 얻으며 죽은 육신을 일으켜 세운다.

그 숫자가 무려 이백. 처음 시도했던 것에 비해 범위도 더욱 넓어졌는지, 저 멀리에 있는 언데드 몬스터들도 스켈레톤 워로드의 통제에 들어와 아군을 공격하기 시작했다.

“와. 너 이 정도였냐?”

- 와. 본 사령관이 이 정도였나?

“…….”

- ……사실 이 정도까지는 아니었다. 하지만 어째서인지는 몰라도, 이곳에 오니 엄청난 마력이 솟구치는구나!

“어, 그래.”

나는 이 괴상한 네임드 몬스터를 이해하기를 포기했다.

하긴 결과만 좋으면 됐지, 지금 당장은 따져 봤자 머리만 아플 것 같다.

- 많은, 더 많은 군단을 내게 다오!

인벤토리에 넣어 둔 터라 보이지는 않지만, 뼈 밖에 안 남은 두개골을 부르르 떨고 있을 것이 분명했다.

나는 한숨을 내쉬며 창을 말아쥐었다.

“안 그래도 그럴 생각이야.”

- 방법이 있나?

“있지.”

더 많은 언데드를 늘리는 방법? 간단하다.

“싹 다 죽이면 돼.”

- 크하하하! 너는 실로 간악하고도 무식한 인간이로구나!

건방진 녀석. 하지만 이번만큼의 놈의 말에 일부분 동의할 수밖에 없다.

머릿속에 울려 퍼지는 스켈레톤 워로드의 광소를 들으며, 나는 걸음을 내디뎠다.

‘염화일로(炎火一路)’

화아아악!

발걸음을 따라, 불꽃의 길이 열렸다.



* * *



새카만 로브와 해골이 주렁주렁 매달린 지팡이. 동공이 있어야 할 그곳은 텅 비어 있었고 몸에는 아직 썩지 않은 살점이 붙어 있었다.

악몽에나 나올 법한 모습을 한 세 존재는 서로를 향해 의념(疑念)을 전달했다.

- 문제가 생겼군.

- 언데드 몬스터들이 통제를 벗어나고 있다. 인간을 도와 군단을 공격하고 있어.

- 어째서?

통제를 벗어나게 한 방법을 묻는 것이 아니다. 그들 세 존재는 이미 그 물음에 대한 답을 알고 있었으니까.

- 상위 언데드다. 우리보다 강력한.

모든 몬스터는 우열이 있지만, 그중에서도 특히 언데드는 철저한 힘의 지배를 받는다.

지금처럼 통제력을 빼앗겼다면 그것은 필시 상위의 존재가 벌인 소행이었다.

- 하지만…….

- 어떻게 그럴 수 있지?

세 존재 중 그 물음에 답할 수 있는 자는 아무도 없었다.

도대체 어찌 자신들보다 강력한 존재가 이곳에 있으며, 언데드의 통제권을 빼앗아 인간을 돕는단 말인가.

- 설마 ‘그분’께서?

- 말도 안 되는 소리. 그분께서 우리를 보내며 내리신 명령을 잊었는가?

- 인간을 죽여라. 더 많은 언데드와 군단을 만들어 더, 더 많은 인간을 죽여라.

명령을 다시금 떠올린 세 존재는 작은 혼란에 빠졌다.

그분, 아크 리치(Arch Lich)가 아니라면 그 누가 자신들의 통제력을 뛰어넘을 수 있단 말인가.

- 인간들 중 네크로맨서가 있었나?

- 아무것도 느끼지 못했다.

- 인간은 죽음을 배척하고 혐오하지. 그럴 리 없어. 설령 있더라도 우리에 비할 바는 아니다.

의념에서 숨길 수 없는 적의(敵意)가 느껴지는 까닭은, 그들 역시 한때 인간의 배척과 멸시를 한 몸에 받았던 네크로맨서였기 때문이었다.

하지만 그것은 이미 아득한 과거이며 또 다른 차원에서 있었던 일.

죽음이라는 망망대해를 표류하던 그들은 아크 리치라는 뱃사공을 만났고, 새로운 힘을 얻어 그토록 염원하던 리치(Lich)로 발돋움하려 하고 있었다.

그러나…….

- 아쉽군.

- 변화가 완전히 끝났더라면. 이 땅에 더 많은 죽음이 있었다면.

- 그럼 통제력을 빼앗기는 일 역시 없었겠지.

세 존재는 안타까움을 금치 못했다.

살아생전 위대한 네크로맨서였던 그들은 아직 완전한 리치로 거듭나지 못한 상태였다.

죽은 마법사의 몸을 빌려 새롭게 태어나기는 했으나, 일주일이라는 시간은 리치로 변화하기 위한 사기(死氣)를 흡수하기에는 너무나도 짧았다.

- 그렇기에 그분께서 우리 셋을 보낸 것인데.

- 이 일이 실패로 돌아간다면 실망하실 거다.

- 우리에게 주신 힘을 도로 빼앗으실지도 몰라.

그건 세 존재가 가장 두려워하는 일이었다.

아크 리치의 신임을 얻기 위해서라면 어떻게든 이 난관을 헤쳐나가야 했다. 설령 극심한 힘을 소모하더라도.

- 어쩔 수 없지.

- 힘을 합치자는 말인가?

- 그렇다. 우리 셋이 힘을 합친다면, 정체를 알 수 없는 상위 언데드도 더는 통제력을 빼앗을 수 없을 것이다.

- 으음. 좋다.

- 동의하는가?

- 동의한다.

아크 리치의 총애를 얻기 위해 경쟁하던 세 존재는 마침내 합의점을 찾았다.

그들은 망설임 없이 사령의 주문을 외우기 시작했다.

- 바렌시아. 마드릿.

- 바이엘른. 뮌헨.

- 스토흐. 시리.

세 존재로부터 흘러나온 죽음의 기운이 대기를 타고 뻗어 나갔다.

푸른 잔디가 까맣게 물들고, 범위에 들어와 있던 인민 해방군 소속의 병사들이 목을 움켜쥐고 쓰러졌다.

“컥!”

“크허억!”

쏴아아악.

단말마와 함께 숨이 끊긴 인간들의 몸에서 흘러나온 사기는 몬스터들의 전신에 스며들었다.

- 캬우우우우!

- 그워어어!

흉포한 외침에 실린 강력한 마력에 주위의 공기가 요동쳤다. 그 힘은 일반적인 몬스터와는 비교도 할 수 없을 정도였다.

강화된 통제력과 휘하 몬스터들의 힘을 느낀 세 존재는 그제야 주문을 멈추었다.

- 키키키키킥.

- 성공이다.

- 엄청난 힘을 소비하긴 했지만…… 이 정도면 차고 넘치는 수준이지.

세 존재가 더욱 강력해진 자신들의 군단을 바라보며 만족스럽게 웃던 그때.

꽈앙!

저 멀리, 굉음과 함께 몬스터의 사지가 날아올랐다.

세 존재는 솟구치는 불꽃을 바라보며 대화를 나누었다.

- 화염 마법사가 있나 보군. 제법인데?

- 그래 봤자 인간이다. 스켈레톤 메이지들을 대거 투입하도록 하지.

- 좋은 생각이야.

그리고 잠시 후, 다시금 솟구치는 화염에 세 존재는 서로를 바라보았다.

- 방금. 뭐였지?

- 통제력이 끊겼다. 빼앗긴 건 아니야.

- 소멸시켰다고? 제법이군.

- 그런데 정말 마법사가 맞나? 움직임이 너무 빠른 것 같은데…….

- 음. 오우거 부대를 투입 시키자.

- 오우거 받고, 듀라한 더.

- 듀라한까지? 그럼 우리들의 호위는 누가 맡지?

- 그의 말이 맞다. 듀라한은 너무 과해. 강화된 오우거로 충분하다.

- 그렇긴 하지.

그리고 삼 분 후.

세 존재의 두개골 위로는 심각한 공기가 어렸다.

- 끊겼다.

- 또?

- 그러게 듀라한 보내자니까.

- 저거 도대체 뭐지. 마법사 아닌 것 같은데.

- 아, 일단 듀라한부터 보내자고!

- 그, 그러도록 하지.

호위부대로 삼은 듀라한 이십여 마리가 우르르 사라지는 모습을 보며, 세 존재는 슬그머니 또 다른 합의점을 찾기 시작했다.

- 음. 그런 일이 벌어지지는 않겠지만 혹시…….

- 나도 비슷한 생각을 했다.

- 데스나이트(Death Knight)…… 만들까?

- 이미 너무 많은 힘을 소비했는데 데스나이트까지? 재료도 마땅치 않고, 시간도 오래 걸릴 텐데.

- 급한 대로 가장 쓸 만한 놈을 골라서 만들면 된다. 우리 셋이 힘을 합친다면 가능해.

- 그, 그럼 시도는 해 볼까.

그러나 세 존재의 데스나이트 제작 계획은 채 십 분도 지나지 않아 산산조각 나고 말았다.

화륵, 콰아아앙!

뼈밖에 남지 않은 몸으로도 느낄 수 있는 초고온의 열기.

“시벌 놈들. 더럽게 많네.”

콰드드득!

겁화(劫火)에 휩싸인 창을 휘두르며 몬스터 군단을 박살 내는 존재를 목격한 세 존재는 황급히 주문을 외웠다.

느릿느릿하던 목소리는 랩처럼 빨라져 있었다.

- 옴느하소유!

- 옌위가지케!

그러나 주문이 완성되기도 전에, 화염 마법사인지 전사인지 분간이 되지 않는 젊은 인간은 그들의 코앞에 도착해 있었다.

“어, 반갑다.”

- 오, 옴느하소유!

- 예, 옌위가지케!

청년, 진태경이 삐딱하게 고개를 꺾었다.

“안녕하세요. 연예가중계? 병신들인가.”
```

## Final English reading copy

```markdown
# Chapter 381

Swoooosh.

I couldn’t see it. But I could feel it. Centered on me—or rather, flowing from the Skeleton Warlord inside the subspace called my inventory—a sticky energy spread in every direction.

The change happened in an instant.

- Krrik?

- Guwo?

The movements of the utterly savage monsters abruptly stopped.

Orcs, trolls, goblins, lycanthropes, every kind of monster I had only ever seen in monster encyclopedias, and even the fallen Hunters.

They had just one thing in common: they had already died once and been resurrected as undead.

Gulp.

I swallowed dryly and muttered.

“This actually works.”

- Wow. It really works.

“……?”

- ……?

*Wait, what did you just say?*

My brain froze for a moment. Then I whispered:

“What kind of boneheaded nonsense was that? Didn’t you do it because you knew it would work?”

The Skeleton Warlord answered sheepishly.

- The truth is… this commander didn’t know it would be this easy.

“You said your control was much stronger.”

- Ah, that? I only said it because I was angry.

“What?”

- I was too proud to just sit there doing nothing…

“……”

*Is this guy completely insane?*

It was absurd, but the result was undeniable.

The undead monsters within a radius of several dozen meters all stopped moving at once, and the fierce battle raging around us briefly fell into a lull.

“Th-The monsters have stopped moving!”

“What on earth is happening?”

“Don’t let your guard down! Some of them are still moving!”

As someone shouted, it was still too soon to relax.

The Skeleton Warlord had only taken control of some of the nearby undead monsters. Those farther away, as well as the ordinary monsters that were not undead, were exceptions.

- Roooooar!

- Kreeeek!

“Haaaaah!”

Clang! Stab!

The uncontrolled monsters were bewildered for only a moment by the sudden change in their own kind before they began rampaging again.

The battle resumed.

It was a fight where the two sides could not even be compared in terms of numbers. But from this moment on, things would be different.

I shouted in a hushed voice.

“Go, Warlordmon!”

The Warlordmon—no, the Skeleton Warlord—shouted angrily.

- You vile human! Do not call this commander that!

“Then what about Warlordmon, who’s dying to disappear?”

- ……Damn it.

Despite being a skeleton that couldn’t even breathe, he let out a deep sigh before beginning to chant a spell.

- Fight, skeleton skeleton.

That bastard had clearly gotten hooked on “skeleton skeleton.” It was an absurdly stupid incantation, but its effect was undeniable.

- Guwo?

At the Skeleton Warlord’s command, ferocity filled the eyes of the undead monsters that had been staring blankly into space.

Then, in the next moment—

Crunch!

An undead ogre’s iron club crushed a troll’s skull.

That was the beginning.

The undead monsters who now served a new master charged toward their former allies.

- Guwoooooo!

- K-Kreeek?

Crack! Slash! Stab-stab-stab!

It was an unexpected ambush from behind.

One flank of the monster army surrounding the Chinese Hunters collapsed helplessly.

- Kreeeeeeek!

“What the hell?!”

“Why are they suddenly…?”

The monsters betrayed by their own kind were not the only ones thrown into confusion.

The Chinese Hunters were bewildered by the sudden turn of events, too. From the front of their formation, I shouted at the young Hunter who had been swinging his spear all over the battlefield.

“Shao Shen!”

“T-Teacher Jin?”

His widened eyes turned toward me.

“How do you know my name?”

I had just checked his Level window using Qi Sense, but that was not important right now.

“What are you doing? Why haven’t you switched to an all-out attack?”

“But what exactly is happening…?”

“Are you really that curious right now? Do you want to grab an undead monster and make it explain why it’s helping us according to the five Ws and one H?”

“No, sir!”

“Then what should we do now?”

Shao Shen suddenly came to his senses and raised his spear high.

“Attack formation! Everyone in the Public Security Armed Forces, attack everything except the undead monsters from this moment onward!”

“Yes, sir!”

*An excellent example of sound judgment.*

With one unified shout, the momentum of the five hundred or so Hunters who had been cornered changed.

“Kill them!”

“Avenge our fallen comrades!”

Swish-swish-swish! Slash!

A lycanthrope charged toward a Hunter who had just cut through an orc’s neck.

The monster opened its jaws, yellow fangs aiming to tear out the Hunter’s throat—but a huge fist slammed into its mouth.

Crunch!

- Grrrrrrr!

The ogre that had crushed the lycanthrope’s skull let out a savage roar.

At that moment, the sharp claws of a griffin diving toward the ogre flashed above its head.

- Screeeeeech!

The griffin let out a piercing cry. Its claws, charged with the mana of an A-rank monster, were just about to rake across the ogre’s eyes when—

“Ice Ball!”

“Lightning Bolt!”

The griffin convulsed in midair after being struck by the spells of the ranged Hunters waiting nearby.

Right then, a figure launched himself upward after stepping on a troll’s shoulder and swung his weapon at the griffin.

“Specially made by J Company, widely regarded as one of Germany’s finest weapon workshops…!”

Slash!

The clean, no-frills strike split the griffin’s head in two.

Team Leader Choi landed gracefully and gazed at the transparent blade, which did not have a single drop of blood on it. He smiled with satisfaction.

“The longsword I won for 5.2 billion won at auction. It really was worth the price.”

“……”

*He looks like an idiot, but he’s cool.*

*He’s cool, but he looks like an idiot.*

The Skeleton Warlord, who had watched the scene, asked in a dubious voice:

- Vile human, you said that man was your superior?

“Technically, yes, in terms of internal Guild positions, but…”

- He looked fairly intelligent for a human. I’ve seen all kinds of strange humans, but this one truly suits you as a superior.

“Raise your hand if you’re a Skeleton Warlord who wants to be annihilated for running his mouth.”

After a brief silence, the Skeleton Warlord answered by chanting another spell.

- Grow, skeleton skeleton!

After three years at a village school, even a dog can recite poetry. By now, he could do it without being told.

Tuk. Tuk-tuk-tuk.

The griffin killed by Team Leader Choi, along with the monsters brought down by the combined attacks of the Hunters and the undead, gained new life and hauled their dead bodies back to their feet.

There were two hundred of them.

The range seemed to have grown even wider compared to his first attempt. Even the undead monsters far away had come under the Skeleton Warlord’s control and begun attacking their former allies.

“Wow. You were this strong?”

- Wow. Was this commander really this strong?

“……”

- ……Actually, this commander was not this strong before. But for some reason, an incredible amount of mana is surging through this place!

“Uh-huh. Good for you.”

I gave up on trying to understand this bizarre named monster.

The important thing was the result. Trying to figure it out right now would only give me a headache.

- Give me a larger legion. A larger one!

I couldn’t see him because he was inside my inventory, but I was certain his skull—which had nothing left but bones—was trembling with excitement.

I sighed and tightened my grip on my spear.

“I was already planning to.”

- Is there a way?

“There is.”

The method for increasing the number of undead was simple.

“You just have to kill every last one of them.”

- Hahahaha! You truly are a vile and brainless human!

*What an arrogant bastard.*

Still, this time, I couldn’t help agreeing with part of what he said.

As the Skeleton Warlord’s mad laughter echoed through my head, I took a step forward.

*Flamefire Path.*

Whoooooosh!

A path of flame opened beneath my footsteps.

* * *

Black robes. A staff with skulls hanging from it.

The places where their pupils should have been were empty, and pieces of flesh that had not yet rotted still clung to their bodies.

The three beings looked as though they had stepped out of a nightmare. They exchanged thoughts with one another.

- A problem has arisen.

- The undead monsters are breaking free of our control. They are helping the humans and attacking the legion.

- Why?

They were not asking how the undead had escaped their control.

The three beings already knew the answer to that question.

- A higher undead. One more powerful than us.

All monsters had a hierarchy of strength, but the undead in particular were ruled completely by power.

If control had been taken away as it had now, it was undoubtedly the work of a superior being.

- But…

- How is that possible?

None of the three beings could answer.

How could an existence more powerful than them be here? How could it steal control of the undead and use them to help the humans?

- Could it be *Him*?

- Don’t be ridiculous. Have you forgotten the order He gave us when He sent us here?

- Kill the humans. Create more undead and a larger legion, then kill more and more humans.

Remembering the order, the three beings fell into a brief state of confusion.

If it was not Him—the Arch Lich—who could possibly surpass their control?

- Was there a necromancer among the humans?

- I sensed nothing.

- Humans reject and hate death. It is impossible. Even if there were one, they would be no match for us.

The reason unmistakable hostility could be felt in their thoughts was that they, too, had once been necromancers who had borne the full weight of human rejection and contempt.

But that had been an unimaginably long time ago, in another dimension.

They had drifted across the boundless sea of death until they encountered a ferryman named the Arch Lich. They gained new power and were now trying to become the Liches they had long yearned to be.

However…

- What a shame.

- If only the transformation had been completed. If only there had been more death in this land.

- Then we would not have lost control, either.

The three beings could not hide their regret.

They had been great necromancers in life, but they had not yet fully transformed into Liches.

They had been reborn by borrowing the bodies of dead mages, but one week was far too short to absorb the death energy needed to transform into Liches.

- That is why He sent the three of us.

- He will be disappointed if this fails.

- He may even take back the power He gave us.

That was what the three beings feared most.

They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s trust—even if it meant expending a tremendous amount of power.

- It cannot be helped.

- Are you suggesting that we join forces?

- Yes. If the three of us combine our power, even this unidentified higher undead will no longer be able to take control from us.

- Hmm. Very well.

- Do you agree?

- I agree.

The three beings had been competing to earn the Arch Lich’s favor, but at last they found common ground.

Without hesitation, they began chanting a necromantic spell.

- Barensia. Madrit.[^1]

- Baielrn. Munich.

- Stoh. Siri.

[^1]: The pseudo-incantation mangles the names Valencia, Madrid, Bayern Munich, and Stoke City.

The energy of death flowing from the three beings spread through the air.

The green grass turned black, and the soldiers of the People’s Liberation Army caught within its range clutched their throats and collapsed.

“Urk!”

“Ghhurk!”

Ssshhhhhh.

The death energy flowing from the bodies of the humans who had died with those final cries seeped into every inch of the monsters.

- Kyaaaaaaa!

- Grrrrrrr!

The air shook beneath the powerful mana contained in their savage cries. Their strength was beyond comparison with ordinary monsters.

Only after sensing the enhanced control and the increased strength of the monsters under their command did the three beings stop chanting.

- Kikikikikik.

- It worked.

- We expended an enormous amount of power, but… this is more than enough.

The three beings were gazing with satisfaction at their strengthened legion when—

BOOM!

Far away, a monster’s limbs flew through the air with a thunderous explosion.

The three beings looked toward the flames surging into the sky.

- There appears to be a fire mage. Not bad.

- It is still only a human. Deploy a large number of Skeleton Mages.

- A good idea.

A short while later, flames surged into the sky again.

The three beings looked at one another.

- Just now. What was that?

- The control was cut off. It was not stolen.

- Did it annihilate them? Impressive.

- But is that really a mage? Its movements seem too fast…

- Let’s deploy the ogre unit.

- I’ll see your ogres and raise you Dullahans.

- More Dullahans? Then who will guard us?

- He has a point. Dullahans are excessive. Strengthened ogres will be enough.

- That is true.

Three minutes later, a grim atmosphere hung over the three beings’ skulls.

- It was cut off.

- Again?

- That is what I said. We should send Dullahans.

- What the hell is that? It does not seem to be a mage.

- I said we should send Dullahans first!

- Th-Then let us do that.

Watching the twenty or so Dullahans they had selected as an escort troop disappear in a group, the three beings cautiously began searching for another point of agreement.

- Hmm. It will not happen, but just in case…

- I had a similar thought.

- A Death Knight… should we make one?

- We have already expended too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time.

- We can choose the most useful one and make it in a hurry. If the three of us combine our power, it is possible.

- Th-Then should we at least try?

But the three beings’ plan to create a Death Knight was shattered into pieces before ten minutes had passed.

Fwoosh! Kaaaa-boom!

Even their bodies made of nothing but bones could feel the heat of the searing flames.

“Fuck, there are a shitload of them.”

Crack-crack-crack!

The three beings saw the figure tearing through the monster legion with a spear engulfed in hellfire and hurriedly began chanting.

Their slow voices had become as fast as rap lyrics.

- Omnehasoyu!

- Yenwigajike!

But before the spell could be completed, the young human—whose identity as either a fire mage or a warrior was impossible to determine—had already arrived right in front of them.

“Uh, nice to meet you.”

- O-Omnehasoyu!

- Ye-Yenwigajike!

The young man, Jin Taekyung, cocked his head to one side.

“Hello. *Entertainment Weekly*?[^2] Are you idiots?”

[^2]: The two incantations sound like mangled versions of *annyeonghaseyo* (“hello”) and *Yeonye-ga Junggye*, the Korean title of the TV program *Entertainment Weekly*.
```
