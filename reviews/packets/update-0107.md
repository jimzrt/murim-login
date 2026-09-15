<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0107.txt",
      "sha256": "696e910b3b030ebbf3fb9da1d4a427c34662c2b93fd08a2eea2d8fd9d8f24827",
      "bytes": 12816
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40f10b9136ba8dfaece2e123bfa9d218ef8ce238630b2642ec360d5e73d09edb",
      "bytes": 4971
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf8acbe4b21a37d67ce4c93a4f9c9d2bfd024d0afd06d2df7afaa87e0881a2a2",
      "bytes": 13960
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9280362eee5e3822d1bd17f2bdbcb75ee8d39002c73f8ff6b8b4824194e580c1",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e7962fd7c5a68a366532839b2b577e73644d1c175e371a05471d37502993703d",
      "bytes": 1221
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "6fdfebc37e517f14edd899eb9c1e7d9c0af606a06021f7907c0a95d189cd3d8a",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "4275611788f171965c4a45fd53783b3f0c3e9e4bf19eee713fcfdde063c7e52f",
      "bytes": 3101
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "38e621a2e538adbc868814d89f00f781ae1e6a6e5c52915d8cb6d1e20a6030af",
      "bytes": 2246
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a05455fcf682929936dc149653dbc807199a561412008c8adebc5f45854eca0",
      "bytes": 14426
    }
  ],
  "estimated_tokens": 17035
}
-->

# Durable State Update — Chapter 107

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 107. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 107. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 107,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 107,
    "continuity_sources": [107],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung; the property being used as its surveillance base remains unidentified.",
    "Choi Byungil led the failed operation against Taekyung and was defeated with the other field Hunters; the Security Team faces written discipline, a pay cut, and possible dismissal.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is an outside B-rank Familiar mage hired by Team Leader 1.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 mage and former Hunter Training Center instructor; he trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown, as does why he now works as a butler.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "Taekyung owns a two-story detached house in Goyang intended as his family's home and will live there alone until Hayeon finishes her college entrance exam; Logout is active, so he no longer needs the capsule to travel between worlds.",
    "Seong Jinho unexpectedly emerged from Taekyung's capsule inside the new house after Taekyung logged into Murim; how and why he entered remains unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin have reached Honju and are staying at the Phoenix Inn's private residence.",
    "Mukyung is a Peak master and uses a superficially learned heat-yang technique to warm Hyuk Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect, now led by Lee Seowol, his uncomfortable former accuser.",
    "Hyuk Mujin is a First Rate martial artist from a tenant-farmer family, Captain of the Jin Family's Gatekeepers, deputy squad leader of White Tiger Hall's reconnaissance squad, and a candidate to become the next Master of the Gatekeeper Pavilion.",
    "Jin Wikyung gave Mujin fifty silver nyang for the journey and ordered the travelers to use good lodging and meals because they had no attendants.",
    "Mukyung considers enduring hunger a form of training, while Taekyung's appetite causes Mujin severe financial anxiety.",
    "The Phoenix Inn attackers were an organized group bearing running-horse tattoos; Wolhwa said Lee Cheonbaek had hired mounted-bandit groups from the northern plateau.",
    "Wolhwa is the Phoenix Inn's proprietress, a courtesan, Shanxi's foremost information merchant, and the Lower District Sect's Shanxi Branch Leader; she has accepted the invitation to accompany Taekyung's group to Mount Heng.",
    "The Lower District Sect's secret wartime pact with the Jin Family promised compensation, but Wolhwa has not yet received it; she wants influence in northern Shanxi, while Jin Wikyung seeks a quiet merger with the Mount Heng Sword Sect.",
    "Wolhwa ordered the Lower District Sect to cancel its investigation into Taekyung and issue a gag order after finding no explanation for his rapid rise."
  ],
  "continuity_sources": [
    106
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and the Mount Heng Sword Sect will react to the invitation and merger proposal remains unknown.",
    "What compensation or territorial concession Wolhwa will ultimately receive from the Jin Family of Taiyuan remains unresolved."
  ],
  "safe_through": 106,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; render 김화종's 춘수 and 교관님 as Chunsoo and Instructor.",
    "Render 1번 훈련생 as Trainee Number One and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 and 계용옥미갱/계용옥미앵 as Phoenix Inn and chicken-and-corn soup.",
    "Render 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's playful Young Master forms for Taekyung and use Young Hero Jin for her 진 소협 address to Mukyung."
  ],
  "version": 1
}
```

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
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |

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
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |

## Exact glossary matches

| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 천무학관   | **Heaven's Gate Temple**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 산서지부장  | **Shanxi Branch Leader**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 보상               | **Reward**                     |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 106
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 106
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 106
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 105
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; leader of the Mount Heng Sword Sect

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 106
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃107화



사두마차는 목적지를 향해 부드럽게 이동했다. 어제와 같은 말, 같은 마차임에도 승차감은 차원이 달랐다. 마부가 교체되었기 때문이다.

겨우 마부석을 벗어나 내 옆자리에 앉은 혁무진이 속 편한 얼굴로 말했다.

“역시 사람은 각자 타고나는 게 있나 봐요. 전 마차 모는 건 영 젬병이라.”

젬병 같은 소리 하네.

하오문 산서지부장인 월화가 데려온 사람이다. 당연히 평범한 마부일 리가 없다.

묵묵하게 말고삐를 잡고 있는 그는 50레벨의 일류 무인이었다. 마부 겸 호위무사, 딱 그림이 나온다.

“무진아.”

“네?”

“제발 조용히 좀 가자. 그럼 중간이라도 간다.”

“……맨날 나만 갖고 뭐라 하셔.”

“네가 맨날 헛소리만 하니까 그렇지, 인마.”

맞은편에 앉아 우리를 지켜보던 월화가 실소를 흘렸다.

“두 사람, 격의 없는 모습이 보기 좋네요.”

“저놈이 싸가지가 없는 겁니다.”

“싸가지라뇨. 이런 말까지는 안 하려고 했는데, 제가 조장보다 두 살이나 더 많습니다. 제 친구들은 애도 있어요.”

“넌 없잖아.”

“아니, 뭐. 그렇긴 한데요.”

“그리고 네가 스물둘이어도 나보다 어려. 아무튼, 어려.”

“그게 무슨 소립니까. 조장님이 이제 겨우 약관인 건 산서성 똥개들도 다 아는 사실인데.”

“못 믿겠으면 한판 붙든가.”

“……다른 분들도 계시니까 여기까지만 하겠습니다.”

혁무진의 추한 변명에 월화가 활짝 웃었다.

“어머, 난 괜찮은데? 여기 진 소협은 어떨지 모르겠지만.”

자연스럽게 모두의 시선이 한 사람을 향해 쏠린다.

아까부터 입을 꾹 다물고 있던 진무경이 움찔하더니 입을 열었다.

“나, 난 상관없소.”

“……?”

뭐야, 저놈 지금 말 더듬은 거야?

예상치 못한 반응에 눈을 동그랗게 뜨고 바라보자 진무경이 슬쩍 시선을 회피했다.

‘어어, 점점.’

원래 저런 캐릭터가 아닌데. 평소 같았으면 뭘 쳐다보냐고 눈을 부라릴 녀석인데.

나는 진심을 담아 물었다.

“어디 아파?”

“……전혀.”

“대화할 때는 사람 눈을 보고 해야지.”

“……시끄럽다. 말 걸지 마.”

오늘따라 참 요상하네, 진짜.

절정 고수씩이나 되는 인간이 마차 멀미에 걸렸을 리는 없고.

아침까지만 해도 팔팔하더니 어째 상태가 영 아니다.

‘그러고 보니까 마차 타고 나서부터 저렇게 된 것 같은데.’

눈을 가늘게 뜨고 진무경을 바라보던 그때.

쿡쿡.

슬쩍 옆구리를 찌른 혁무진이 내게만 들릴 정도로 작은 목소리로 속삭였다.

“이공자님 좀 보세요.”

“뭐가…… 아.”

혁무진의 말을 들은 후에야 이상한 광경이 눈에 띄었다.

어떻게 지금까지 눈치채지 못했나 싶을 정도다.

‘뭐지?’

태원진가에서 가져온 사두마차는 상당히 호화롭다. 어지간한 방 하나 크기라 좌석도 넓었다. 지금 인원의 두 배를 태워도 무리가 없을 정도다.

그런데…….

‘쟤는 왜 저러고 있어.’

현재 진무경은 넓은 좌석을 두고 마차 끄트머리 구석에 몸을 구겨 넣고 있었다. 아니, 저 정도면 거의 압축 수준이다.

‘9와 4분의 3 승강장이야, 뭐야.’

천무학관이 아니라 마법 학교를 다니고 있는 건가.

한편 저 괴상한 짓거리를 지켜보고 있는 것은 나와 혁무진만이 아니었다.

“진 소협. 많이 불편해 보이는데 이쪽으로 좀 오세요. 자리 많이 남아요.”

월화의 고혹적인 목소리에 덜컥 굳는 진무경의 신형.

삐걱거리는 대답이 흘러나온 건 잠시 후였다.

“괘, 괜찮소.”

“…….”

하나도 안 괜찮아 보이는데. 나와 비슷한 표정을 짓고 있는 혁무진에게 조용히 속삭였다.

“네가 봐도 이상하지?”

“이상한 정도가 아닌데요.”

“그래, 나도 비슷한 생각이야.”

우리는 의미심장한 눈빛을 주고받았다.

“세상에, 누가 상상이나 했겠습니까.”

“그러게. 천하의 진천검이 저렇게 낯가림이 심할 줄이야.”

“제 말이 그 말…… 예?”

“반응이 왜 그래? 사람 성격 가지고 뭐라 하면 안 돼. 나처럼 낯짝 두꺼운 놈이 있으면 소심한 사람도 있는 거야.”

“아니, 잠시만. 잠시만요.”

혁무진이 더듬거리며 말을 이었다.

“지금 무슨 말씀을 하시는 거예요?”

“그야 당연히 진무경…….”

으스스한 목소리가 불쑥 끼어들었다.

“입 다물어.”

아무리 넓어 봤자 마차 안이니 다 들린다. 진무경의 찢어 죽일 듯한 눈빛에 나와 혁무진이 동시에 입을 다물었다.

살벌한 분위기를 환기시킨 건 월화였다.

“내 정신 좀 봐, 아직 정식으로 인사드린 적이 없네요. 하오문 산서지부장 월화라고 합니다.”

“……태원진가의 진무경이오.”

“반응이 영 심심하네요. 저기 진 공자는 처음 제 신분을 듣고 엄청나게 놀랐는데.”

“저 녀석에게 대충 들어서 알고는 있었소. 본가를 위해 큰일을 해 주셨다는 이야기도.”

진무경이 정중하게 포권을 취했다.

“늦었지만 감사를 표하오.”

“별말씀을. 정당한 거래였어요.”

월화가 매끄럽게 한 마디를 덧붙였다.

“아직 적절한 보상은 못 받았지만요.”

“본가는 하오문의 호의를 잊지 않을 거요.”

아직도 어색하기 짝이 없는 행동과 말투지만 그래도 처음보다는 썩 나아진 모습이다.

미남과 미녀의 그림 같은 투샷에 혁무진이 감탄사를 토했다.

“촉망받는 젊은 고수와 절세의 미녀라…… 크으, 보기만 해도 가슴이 뛰는군요. 안 그렇습니까?”

나는 못 들은 척 고개를 돌렸다.

피부가 따끔거릴 정도로 살기 어린 시선을 보아하니, 혁무진의 가슴이 뛸 시간은 얼마 남지 않은 게 분명했다.



* * *



겨울의 낮은 성미가 급하다.

산길을 따라 얼마나 이동했을까, 금세 해가 지고 어둠이 찾아왔다. 마차가 멈춘 것은 그로부터 두 시진이 지난 후, 자정 무렵이었다.

“도착했습니다.”

마차에서 내리자마자 보이는 것은 적당한 크기의 목제 건물이었다.

안으로 발을 내딛자마자 느껴지는 싸늘한 공기. 사람을 본뜬 동상은 위엄 있게 우리를 내려다보고 있었다. 이런 곳을 뭐라고 하더라?

‘아, 그래. 사당(祠堂).’

죽은 이의 위패를 모시고 제사를 지내는 장소라고 들었다.

무협 소설에서 심심하면 등장하는 관제묘(關帝廟)가 떠올라 동상을 살펴봤지만 누군지는 알 수 없었다.

“수년 전 기근 이후로 버려진 사당인데, 지금도 간혹 인근 양민들이 오는 모양이에요.”

월화의 말처럼 사당 내부는 휑했지만 아직 사람의 흔적이 남아 있었다. 이를테면 먼지 쌓인 바닥 위로 찍혀 있는 사람의 발자국이라든가.

“자리를 준비하겠습니다.”

하오문도로 짐작되는 마부 겸 호위무사의 말에 우리는 사당 밖으로 나왔다. 아니, 정확히 말하면 한 명은 누군가에 의해 끌려 나왔다고 해야 맞겠다.

“따라와라.”

“으헉, 조장님, 조장님!”

진무경에게 멱살을 잡힌 채 질질 끌려가는 혁무진을 외면하고 하늘을 바라봤다. 음, 오늘은 달이 참 밝구나.

“뭐 해요?”

“뭐, 보시는 대로죠.”

월화가 싱긋 웃었다.

“경치 구경하는 거 좋아하나 봐요?”

“요즘 들어서 좋아지고 있어요.”

현대에서 볼 수 있는 경치라고 해 봐야 높은 곳에서 내려다보이는 야경이다. 그마저도 직장인들의 야근이 만들어 낸 슬픈 불빛들이고.

‘이런 게 진짜 경치지.’

빽빽한 빌딩 숲도, 아파트 단지와 공장 부지도 없다.

아스팔트 도로 대신 축축한 흙길과 청량한 공기가 온 세상에 가득하다.

‘이런 곳에서 살면 힐링 제대로 될 텐데.’

문제는 킬링 당하기도 쉬운 동네라는 거다. 어떻게 된 게 여기는 몬스터보다 사람이 더 무섭다.

굳이 대장로나 조필까지 갈 필요도 없이, 바로 어제 봉황객잔에서 있었던 일만 해도 그렇다.

“아, 맞다. 그놈들은 어떻게 됐어요?”

“적풍단(赤風團)의 마적들을 말하는 거라면 구금해 뒀어요. 물론 그 전에 의원을 불러야 했죠.”

그 정도로 개박살을 내 줬으니 치료가 필요하긴 했을 거다.

그러나 그보다 관심을 끄는 단어가 있었다.

“적풍단이요?”

“고원에서 떠오르는 신흥 강자예요. 규모도 제법 크고, 무엇보다 우두머리인 적풍단주의 무공이 고강하다고 알려져 있어요.”

북부 고원. 항산검문과의 전쟁 당시 지도를 통해 처음으로 알게 된 지명이다.

한 가지 의아한 점은, 봉황객잔이 있는 혼주와 고원의 거리가 상당하다는 것이었다. 밤낮으로 말을 달려도 일주일 이상이 소요되는 걸로 알고 있는데…….

“그런 놈들이 어떻게 여기까지 흘러들어온 겁니까?”

“이천백은 전쟁 말미에 수많은 낭인과 마적단들을 고용했어요. 그중 상당수는 팔천협에서 뼈를 묻었지만, 일부는 살아남아 도망쳤죠.”

“그중에 적풍단이 있었다?”

월화가 고개를 저었다.

“적풍단주…… 생각 이상으로 머리 회전이 빠른 자더군요.”

“그럼?”

“그는 마지막까지 사태를 지켜봤어요. 불과 두 시진 떨어진 거리에서 팔천협을 예의 주시하다가 전투 결과를 듣고 말 머리를 돌렸죠. 자신을 따르는 이백 명의 수하와 함께.”

자그마치 이백 명.

만약 그날 팔천협에서 적풍단이 가세했다면 어떻게 되었을까? 엄청난 사상자가 나오는 건 물론이고 전투의 승패에도 영향을 끼쳤을지도 모른다.

“우리로서는 행운이었네요.”

“그렇죠. 항산검문 입장에서는 엄청난 불운이었고.”

월화가 곰방대에 담뱃잎을 꾹꾹 눌러 담으며 말을 이었다.

“적풍단은 그 길로 북상했어요. 대부분의 병력이 빠져나간 항산검문의 본진을 노린 거죠.”

“……허.”

그야말로 타고난 약탈자다.

전쟁의 승기가 한쪽으로 기울자마자 북상, 대부분의 주력이 빠져나간 항산검문의 목덜미를 물어뜯은 것이다.

전투에 참여하지 않은 덕분에 병력을 보존한 건 물론이고 충분한 휴식도 취했을 테니, 컨디션은 최상이었겠지.

“결과는 진 공자도 들어서 알죠?”

“네.”

이틀 동안 이어진 치열한 전투는 결국 항산검문의 승리로 막을 내렸다. 아버지를 뒤를 이어야 할 소문주의 죽음을 남기고.

“그런데 제가 들은 소문으로는 낭인과 마적들이 섞여 있었다고 하던데요.”

“호랑이가 이빨이 빠졌다고 해서 개라고 부르진 않는 법. 적풍단주가 끌어들인 낭인들도 제법 되죠. 방패막이로 사용하기에는 딱 좋았을 테니까.”

탁, 탁.

화섭자를 꺼내 불을 붙인 그녀가 곰방대를 빨아들였다.

“진 공자가 쓰러트린 마적들은 아마도 그때 도망친 자들일 거예요. 적풍단이 마적단치고 제법 규율이 강하긴 해도 탈영병이 아예 없진 않으니까. 혼주에서 뭘 하고 있었는지는 잘 모르겠지만요.”

“탈영병이라…….”

“그것 때문에 근래 들어 이 근방이 어수선해요. 낭인, 산적, 마적, 심지어는 흑도들까지 슬쩍 고개를 들고 있는데 항산검문의 힘은 형편없이 줄어들었으니까.”

“우리의 제안을 받아들일 수밖에 없겠네요.”

월화가 새치름하게 웃어 보였다.

“정확히 말하면 우리, 가 아니라 태원진가겠죠? 뭐, 내 입장에서도 신임 문주를 핍박하기 좋은 때라는 건 맞지만.”

“저기, 그런데요.”

“응?”

“이런 날씨에도 사당에 오는 양민들이 있습니까?”

“그럴 리가요. 사냥꾼들이라면 몰라도. 그런데 갑자기 그건 왜?”

나는 산길을 가리켰다. 어느새 휘날리기 시작한 엷은 눈보라 사이로, 이쪽을 향해 올라오는 횃불들이 보였다.
```

## Final English reading copy

```markdown
# Chapter 107

The four-horse carriage moved smoothly toward its destination. Even though it was the same carriage pulled by the same horses as yesterday, the ride was on an entirely different level.

The driver had been replaced.

Hyuk Mujin, who had finally escaped the driver’s seat and settled beside me, said with a relaxed expression,

“People really must be born with different talents. I’m hopeless at driving a carriage.”

*What a load of crap.*

He was someone Wolhwa, the Lower District Sect’s Shanxi Branch Leader, had brought with her. Naturally, there was no way he was an ordinary coachman.

The man quietly holding the reins was a Level 50 First Rate martial artist. A coachman and a bodyguard. The picture fit perfectly.

“Mujin.”

“Yes?”

“Please just travel quietly. Then you’ll at least do okay.”

“……Why am I always the one you pick on?”

“Because you’re always spouting nonsense, you idiot.”

Wolhwa, who was sitting across from us and watching, let out a quiet laugh.

“You two seem very comfortable with each other.”

“He’s just rude.”

“Rude? I wasn’t going to say this, but I’m two years older than the squad leader. My friends have children.”

“You don’t.”

“Well, no. That’s true.”

“And even if you were twenty-two, you’d still be younger than me. Anyway, you’re younger.”

“What are you talking about? Even the stray dogs of Shanxi Province know that the squad leader is barely twenty.”

“If you don’t believe me, then let’s have a match.”

“……Since there are other people here, I’ll stop at this point.”

Wolhwa smiled brightly at Hyuk Mujin’s ugly excuse.

“Oh, I don’t mind. Though I can’t speak for Young Hero Jin.”

Everyone’s eyes naturally turned toward one person.

Jin Mukyung, who had kept his mouth tightly shut until then, flinched and opened it.

“I—I don’t mind.”

“……?”

*What the hell? Did he just stutter?*

I stared at him with my eyes wide open at the unexpected response. Jin Mukyung subtly looked away.

*Oh, this is getting worse.*

He wasn’t usually like this. Normally, he would have glared and asked what I was staring at.

I asked him sincerely,

“Are you sick?”

“……Not at all.”

“When you’re talking to someone, you should look them in the eye.”

“……Be quiet. Don’t talk to me.”

He was acting really strange today.

There was no way a Peak master like him had gotten motion sickness.

He had been full of energy until this morning, but now he was clearly not himself.

*Come to think of it, he seems to have been like this ever since we got into the carriage.*

Just as I was narrowing my eyes and watching Jin Mukyung—

*Poke, poke.*

Hyuk Mujin nudged me in the side and whispered so quietly that only I could hear him.

“Look at the Second Young Master.”

“Look at what…… Ah.”

Only after hearing Hyuk Mujin did I notice the bizarre sight.

I couldn’t believe I hadn’t noticed it until now.

*What is he doing?*

The four-horse carriage brought from the Jin Family of Taiyuan was quite luxurious. The inside was about the size of an ordinary room, and the seats were spacious too. It could have carried twice as many people as we had without any trouble.

And yet…

*Why is he sitting like that?*

Jin Mukyung had ignored the spacious seats and folded himself into the corner at the very end of the carriage.

No, “folded” didn’t quite cover it. He was practically compressed.

*What is this, Platform Nine and Three-Quarters?*

Was he attending a magic school instead of Heaven’s Gate Temple?

I wasn’t the only one watching this strange behavior.

“Young Hero Jin, you look very uncomfortable. Why don’t you come over here? There’s plenty of room.”

Jin Mukyung’s body went rigid at the sound of Wolhwa’s alluring voice.

A creaking reply came a moment later.

“I—I’m fine.”

“……”

He didn’t look fine at all.

I whispered quietly to Hyuk Mujin, whose expression was similar to mine.

“You think he’s acting strange too, right?”

“It’s more than strange.”

“Yeah. I thought so too.”

We exchanged meaningful glances.

“My goodness. Who could have imagined this?”

“Exactly. Who knew the Heaven Shaking Sword was so shy around people?”

“That’s exactly what I mean…… Huh?”

“Why are you reacting like that? You shouldn’t criticize someone’s personality. If there are thick-skinned guys like me, then there can be timid people too.”

“No, wait. Just wait a moment.”

Hyuk Mujin stumbled over his words.

“What exactly are you talking about?”

“Obviously, Jin Mukyung……”

An eerie voice suddenly cut in.

“Shut up.”

No matter how spacious the carriage was, everyone inside could hear everything.

Under Jin Mukyung’s murderous glare, Hyuk Mujin and I shut our mouths at the same time.

Wolhwa was the one who changed the grim atmosphere.

“Where are my manners? I haven’t even properly introduced myself yet. I’m Wolhwa, Shanxi Branch Leader of the Lower District Sect.”

“……I am Jin Mukyung of the Jin Family of Taiyuan.”

“What a dull reaction. That Young Master Jin over there was extremely surprised when he first heard about my identity.”

“I heard the general details from him. I also heard that you did a great deal for our family.”

Jin Mukyung politely clasped his hands.

“I realize this is late, but allow me to express my thanks.”

“Not at all. It was a fair trade.”

Wolhwa smoothly added,

“Though I haven’t received the proper compensation yet.”

“Our family will not forget the Lower District Sect’s goodwill.”

His behavior and speech were still awkward beyond belief, but he was doing much better than when they had first met.

Looking at the handsome man and beautiful woman sitting together like a picture, Hyuk Mujin exclaimed,

“A promising young martial arts master and a peerless beauty… Whew, just looking at them makes my heart race. Don’t you agree?”

I turned my head away and pretended not to hear him.

Judging by the killing intent prickling my skin, Hyuk Mujin’s heart wouldn’t be racing for much longer.

* * *

Winter days were short-tempered.

How long had we traveled along the mountain road? The sun quickly set, and darkness descended. The carriage stopped four hours later, around midnight.

“We’ve arrived.”

The first thing I saw after stepping out of the carriage was a moderately sized wooden building.

The moment I stepped inside, I felt a chill in the air. A statue shaped in the likeness of a person looked down at us with solemn dignity.

*What did they call places like this again?*

*Oh, right. A shrine.*

I had heard that it was a place where the spirit tablets of the dead were kept and memorial rites were performed.

The Guandi Temples that appeared so often in martial arts novels came to mind. I looked closely at the statue, but I couldn’t tell who it represented.

“It’s a shrine that was abandoned after a famine several years ago, though it seems local commoners still come here from time to time.”

Just as Wolhwa had said, the inside of the shrine was empty, but traces of human presence remained. For example, there were footprints pressed into the dust-covered floor.

“I’ll prepare the place.”

At the words of the coachman and bodyguard, whom I assumed was a member of the Lower District Sect, we went outside the shrine.

More precisely, one of us was dragged out by someone.

“Follow me.”

“Gah! Squad Leader! Squad Leader!”

I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky.

*The moon is awfully bright tonight.*

“What are you doing?”

“As you can see.”

Wolhwa smiled faintly.

“You seem to enjoy looking at the scenery.”

“I’ve been starting to enjoy it lately.”

The only scenery available in the modern world was a night view seen from some high place. Even that consisted of sad lights created by office workers working overtime.

*This is real scenery.*

There were no dense forests of skyscrapers, no apartment complexes, and no factories.

In place of asphalt roads, damp dirt paths and crisp air filled the entire world.

*Living in a place like this would be genuinely healing.*

The problem was that it was also an easy place to get killed.

Somehow, people were more frightening here than monsters.

I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough.

“Oh, right. What happened to those guys?”

“If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.”

I’d beaten the shit out of them, so of course they’d needed treatment.

But there was another word that caught my attention more than that.

“The Red Wind Band?”

“They’re a rising power from the plateau. They’re fairly large, and more than anything, the leader of the Red Wind Band is said to possess formidable martial arts.”

The Northern Plateau.

I had first learned of that place through the map during the war with the Mount Heng Sword Sect.

One thing struck me as strange: the plateau was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, it took more than a week even if one rode day and night.

“How did people like that end up all the way here?”

“Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.”

“So the Red Wind Band was among them?”

Wolhwa shook her head.

“The leader of the Red Wind Band…… He was quicker-witted than I expected.”

“What do you mean?”

“He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only four hours away, then turned his horse around when he heard the outcome of the battle.”

“With the two hundred subordinates who followed him.”

Two hundred people.

What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle.

“We were lucky.”

“We were. For the Mount Heng Sword Sect, it was incredibly unlucky.”

Wolhwa continued as she packed tobacco into her long-stemmed pipe.

“The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.”

“……Huh.”

They were natural-born plunderers.

The moment the tide of the war turned, they headed north and bit into the throat of the Mount Heng Sword Sect, whose main forces had already withdrawn.

They had preserved their forces by not participating in the battle, and they must have gotten plenty of rest as well. Their condition would have been at its peak.

“Young Master Jin, you heard what happened, didn’t you?”

“Yes.”

The fierce battle that continued for two days ended with the Mount Heng Sword Sect’s victory.

It also left behind the death of the Young Sect Leader, who was supposed to succeed his father.

“But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.”

“A tiger doesn’t become a dog just because it has lost its teeth. The wandering martial artists the leader of the Red Wind Band drew in were fairly numerous as well. They would have been perfect for use as shields.”

*Tap, tap.*

Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe.

“The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.”

“Deserters……”

“That’s why things have been chaotic around here lately. Wandering martial artists, bandits, mounted bandits, and even dark-path figures are starting to raise their heads, while the Mount Heng Sword Sect’s strength has been reduced to almost nothing.”

“They’ll have no choice but to accept our proposal.”

Wolhwa smiled demurely.

“To be precise, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is indeed a good time to pressure the new Sect Leader.”

“By the way……”

“Yes?”

“Do commoners really come to this shrine in weather like this?”

“Of course not. Hunters, perhaps. Why do you ask all of a sudden?”

I pointed toward the mountain path.

Through the thin snowstorm that had begun to swirl, I could see torches climbing toward us.
```
