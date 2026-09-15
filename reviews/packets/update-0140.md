<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0140.txt",
      "sha256": "b74218fb7d519f1cb5205581c45ccc6128b5e063a2188656e5b91a7fdd5b73bf",
      "bytes": 16965
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "22fc1d89285bb48c8314b5b29129c483d539068fd3be94c140856810e847dc93",
      "bytes": 2528
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "21a50d0432f268fc5aa34ed9872944ccc374d40691d6855153ba6586b4aead04",
      "bytes": 29151
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b30ae34549e15c077ce54f19530ea0fb6ea497ac862783ce59f27bc74b0d94ef",
      "bytes": 755
    },
    {
      "path": "characters/Gong Ilhyuk.md",
      "sha256": "69430821cd41d193bd9e0db60b4a829a4a5b997f1956dec0956e086ca03010cd",
      "bytes": 530
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "f62ec5fc30c8fbe7930d38e6f01fe5c2387cb9f711dc6edae182f96c6b21de0a",
      "bytes": 638
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7b27efe55e94bc96ad672ad1cebc2dcdc0466c6a9f51f7ba30dd6153bdb11660",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5af22d3107e892d383bc856fb9ce8c36341a2c74e542022f389c5d075e62f7a0",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "56a2280084a473a4c1bc7dc73cc563288cd13b6d47ebc06c13695ddd37c42a0f",
      "bytes": 594
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "618d1ee36424025899be8aa6c1eab32f0d6d1ff13215897dc503cc42d134b3be",
      "bytes": 23850
    }
  ],
  "estimated_tokens": 25242
}
-->

# Durable State Update — Chapter 140

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 140. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 140. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 140,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 140,
    "continuity_sources": [140],
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
    "The Jin Family procession reaches the Shanxi Provincial Office for the City Lord's luncheon.",
    "The Shanxi Provincial Office is a palace-like fortified complex that can accommodate several thousand people and holds enough grain to endure ten years of wartime defense.",
    "The soldiers stationed at the Shanxi Provincial Office are highly trained: most guards are around Level 20, commanders exceed First Rate, and units practice synchronized spear formations.",
    "Cheongpung does not understand the etiquette surrounding royalty and must be told to address the resident prince as His Highness rather than king.",
    "The official escorting the young prodigies is deeply afraid that Cheongpung will make an inappropriate remark and repeatedly asks Taekyung to keep him quiet.",
    "A tense discussion is already underway at the luncheon before Taekyung's group enters; fragments mention the Assistant Military Commissioner, Huashan, and an insult.",
    "Hong Jin is a Level 22 man with a delicate appearance and voice who interrupts the tense exchange and flatters Taekyung while greeting him.",
    "Li Feng is a Level 68 man in black martial robes whose appearance and bearing suggest affiliation with the military.",
    "Three additional young martial artists at the luncheon identify themselves as members of the Zhongnan Sect of Shaanxi and treat Taekyung as a junior.",
    "Taekyung identifies himself as Jin Taekyung of the Jin Family of Taiyuan, causing the hostile atmosphere around the other four men to ease somewhat.",
    "Taekyung recognizes the Zhongnan Sect from reading about it in what he thought was a novel, then stops himself before completing the reference."
  ],
  "continuity_sources": [
    139
  ],
  "open_questions": [
    "What conflict involving the Assistant Military Commissioner, Huashan, and an insult preceded Taekyung's arrival at the luncheon?",
    "What are the names and individual identities of the three Zhongnan Sect martial artists?",
    "What was Taekyung about to say after recognizing the Zhongnan Sect from the novel?"
  ],
  "safe_through": 139,
  "temporary_decisions": [
    "Render 전하 as “His Highness” when used as the formal royal address.",
    "Render 왕 as “king” when Cheongpung uses it literally, while preserving the official correction to “His Highness.”",
    "Render 초일류 as “advanced First Rate.”",
    "Render 군문 as “military” when describing an affiliation."
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
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |

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
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일중    | **Gong Iljung**    |
| 공일혁    | **Gong Ilhyuk**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 권법     | **fist technique**                               |                                                       |
| 장법     | **palm technique**                               |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 큰형     | **eldest brother**                           |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 139
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Gong Ilhyuk.md

# Gong Ilhyuk (공일혁)

- **Safe through:** Chapter 138
- **Aliases:** None
- **Role:** The third member of the Three Hands of Zhongnan and a Zhongnan Sect martial artist from Shaanxi
- **Personality:** Sharp-tongued, mocking, and openly antagonistic toward Li Feng
- **Voice:** Casual, taunting, and deliberately provocative
- **Relationships:** Member of the Zhongnan Sect's Three Hands; involved in a ten-year-old humiliating martial grievance with Li Feng

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 139
- **Aliases:** None
- **Role:** Level 22 man attending the City Lord's luncheon; he interrupts a tense exchange and greets Jin Taekyung as a young hero of the Jin Family of Taiyuan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 139
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 139
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 139
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; political rival of Eunuch Hong; bears a humiliating martial grievance involving Gong Ilhyuk

## Korean source

```text
＃140화



종남삼수(終南三手) 공일혁은 떨떠름한 표정으로 눈앞의 청년을 바라봤다.

‘뭐지, 이놈은?’

산서잠룡 진태경. 불과 몇 달 만에 섬서성까지 슬금슬금 이름을 알리고 있는 돌풍의 주역이다.

공일혁은 속으로 진태경이 했던 말을 곱씹었다.

‘군림…… 뭐라고?’

분명히 무슨 말을 하려다 말았던 것 같은데.

처음 종남파의 이름을 들었을 때 보여 줬던 열광적인 반응과 달리, 놈은 지금 김이 팍 샌 얼굴로 한숨만 푹푹 내쉬고 있었다.

“휴우.”

“……웬 한숨인가?”

“아닙니다. 아무것도 아니에요.”

“아니긴 뭐가 아닌가? 그러지 말고 마저 말해 보게.”

공일혁은 슬슬 기분이 나빠지기 시작했다. 자신의 사문이 어떤 곳인가, 바로 그 유명한 종남파(終南派)다.

수백 년의 역사와 뿌리 깊은 무맥을 바탕으로 당당히 구파일방(九派一幇)에 이름을 올린 무림의 거목 중 하나란 말이다.

그런데…….

‘알아봐 주는 것에 감사하지는 못할망정 한숨을 내쉬어?’

태원진가가 아무리 잘나가 봐야 아직은 변방의 일개 가문에 불과하다.

구파일방인 종남파와 비교하면 태양 앞의 반딧불 같은 존재. 출신 배경으로나, 개인의 명성으로나 까마득한 애송이 녀석이다.

‘시건방진 놈.’

종남파의 제자라는 자부심으로 평생을 살아 온 그다. 기분이 나쁜 것도 당연했다.

공일혁과 함께 종남삼수로 불리는 다른 두 사람 역시 진태경을 보는 시선이 곱지 않았다.

“크흠.”

“젊은 친구가 말을 하다가 마는 버릇이 있군.”

분위기가 영 텁텁해지자 진태경이 손을 내저었다.

“아뇨, 그런 게 아니고요. 그냥 혼자 착각했던 것뿐입니다.”

공일혁이 애써 너그러운 말투로 입을 열었다.

“무슨 착각? 말해 보게. 내 다 대답해 줄 터이니.”

“진짜 별거 아닌데…….”

“아, 말해 보라고!”

“엥, 왜 소리를 지르고 그러세요?”

공일혁은 호흡을 가다듬었다.

내일모레면 그의 나이 불혹이다. 그런데 이제 겨우 약관밖에 안 된 어린놈에게 이렇게 흥분하다니.

이상하게 저놈의 잘생긴 얼굴을 보고 있으면 약이 오르는 기분이다.

“그게 아니고…… 후우, 어쨌든 말해 보게.”

“으음.”

진태경이 어쩔 수 없다는 듯이 입을 열었다.

“그럼 하나만 여쭤봐도 되겠습니까?”

“뭐든지.”

“지금 종남파 회장님, 아니 장문인 존함이 어떻게 되시는지?”

“응? 장문인의 존함 말인가?”

“네.”

이게 무슨 뜬금없는 질문이란 말인가? 공일혁은 의아함을 느끼며 대답했다.

“공씨 성에 일 자, 중 자 쓰시네.”

“아아, 네.”

마치 그게 누구냐는 듯 심드렁한 대답이다. 공일혁을 포함한 세 사람의 이마에 핏대가 섰다.

“장문인의 존함을 들어 본 적 없나?”

진태경이 뒤통수를 긁적였다.

“글쎄요, 들어 본 것 같기도 하고. 아닌 것 같기도 하고…….”

“……그, 그럼 풍운검군(風雲劍君)이라는 별호는?”

“풍운검군 공일중, 풍운검군 공일중…… 쓰읍, 잘 모르겠는데요.”

기가 찰 노릇이다. 구파일방, 오대세가의 장문인과 가주들은 모두 천하에 이름이 쟁쟁한 고수들. 무림인이라면 모를 수 없는 존재다.

하물며 얼뜨기 무인도 아니고 태원진가의 자제라는 놈이 종남파 장문인을 모르다니.

심지어 제 친구라도 되는 마냥 이름을 불러 댄다.

‘이놈이 지금 종남파를 우롱하는 건가?’

공일혁이 충격으로 머리가 띵해 있는데, 문득 진태경이 고개를 들어 그를 바라봤다.

“어? 그러고 보니 이름이 비슷하시네요. 공일중, 공일혁.”

그나마 최소한의 눈치는 있는 놈이군. 공일혁의 심기가 살짝 누그러졌다.

“집안 어른이시네.”

“오, 집안 어른! 그럼 혹시 관계가…….”

“오촌 당숙 되시지.”

“오촌 당숙!”

눈이 휘둥그레진 진태경을 보자 공일혁의 어깨에 힘이 들어갔다.

다른 사람도 아니고 풍운검군이다. 종남파의 장문인과 한집안 사람이라는 건 엄청난 영광 아닌가.

“크흠, 너무 소문내지는 말아 주게. 아무래도 이 사실이 널리 알려지면 사람들이 날 대하는 태도가 달라질 테니 말일세.”

실제론 이 사실이 누구보다 알려지길 원하는 건 공일혁 본인이다.

그는 지금까지 풍운검군의 이름을 앞세워 온갖 혜택을 누려 왔다. 뛰어난 무공과 영약, 그리고 종남삼수라는 별호까지.

이대로만 승승장구를 거듭한다면 종남파의 요직을 꿰차는 것도 시간문제였다.

“내 말, 잘 알아들었지? 정 말하고 싶다면 가까운 벗 몇 명한테만…….”

진태경이 손을 내저었다.

“에이, 절대 말 안 합니다. 공 대협 평판에 누가 될 게 뻔한데. 연줄 믿고 여기까지 올라온 놈, 어이쿠. 죄송합니다. 어쨌든 그런 식으로 소문나면 곤란하잖아요.”

공일혁은 헛기침을 내뱉었다. 스스로 생각하기에도 아주 틀린 얘기는 아니었기 때문이다.

“크흠. 딱히 누가 될 것까지야 있겠나. 내 말은, 혹 나에 대해 궁금해하는 사람이 있을 수 있으니…….”

“궁금해하는 사람이요? 저 친구 한 명도 없어서 딱히 말해 줄 사람이 없는데.”

“……자네 큰형님인 진 소가주나, 아니면 진천검 소협이 궁금해할 수도 있지 않겠나?”

“아, 저희 가문 사정 잘 모르시는구나. 큰형님 지금 엄청 바빠요. 둘째 형은 무공 아니면 별 관심도 없고.”

“……그래?”

“예.”

그렇다는데 더 할 말도 없다. 언짢은 헛기침만 연발하는 그를 보며 진태경이 해맑게 웃었다.

“그리고 그거 말해 봤자 뭐해요. 오촌 당숙이면 거의 남이나 다름없는데. 저는 또 무슨 부자지간이라도 되시는 줄.”

“……!”



* * *



역시 웃는 얼굴로 엿 먹이는 게 세상에서 제일 짜릿하다.

특히 거만 떠는 놈들한테는 제대로 먹이기만 하면 쾌감은 두 배가 된다.

‘아, 중독될 것 같아.’

종남삼수라고 했나?

처음부터 마음에 안 들었던 놈들이다. 위에서 내려다보는 듯한 눈빛도, 대문파랍시고 거들먹거리는 태도도.

‘역시 소설이랑은 다르네.’

고등학교 다닐 때는 종남파 제자가 되는 게 꿈이었는데, 역시 현실은 시궁창이다.

나는 주먹을 부르르 떠는 공일혁을 보며 새어 나오는 웃음을 참았다.

‘귀여운 자식, 놀리는 맛이 쏠쏠하네.’

더 놀려 주고 싶지만 이쯤 해 둬야 한다. 태원진가가 지역구라면 저쪽은 전국구. 시비 붙어서 좋을 게 없으니까.

다행히 불쑥 끼어든 목소리가 분위기를 환기시켰다.

“너무 그쪽 분들만 대화하시는 거 아니에요? 다른 분들 외로우시겠다. 아직 소개도 다 못 했는데.”

콧소리가 듬뿍 들어간 간드러진 목소리에 한 번.

나를 보며 찡긋 웃는 미중년의 모습에 두 번 소름이 돋는다.

“아직 내 소개를 못 했죠? 산서성 도지휘동지, 홍진이라고 해요.”

“도지휘……뭐요?”

“도지휘동지요. 아, 무림인이시라 이런 직책은 처음 들어 보시는구나?”

“네.”

위원장 동지는 들어 봤어도 도지휘동지는 처음 들어 보네.

눈만 껌뻑이는 나를 보며 홍진이 까르르 웃었다. 세상에, 중년 남성이 까르르 웃다니.

“표정이 왜 그래요? 무슨 안 좋은 일이라도?”

“……아뇨. 너무 행복해서.”

“행복? 호호호, 너무 귀여우시다. 안 그래요, 이 첨사?”

귀엽대 시발, 저 새끼가 나한테 귀엽대.

간신히 구역질을 참고 있는데 앞서 스치듯이 본 이풍이라는 사내가 무뚝뚝하게 인사를 건넸다.

“산서성 도지휘첨사 이풍이오. 산서성부 소속 군사들의 훈련을 맡고 있지.”

“그리고 내 직속 부하죠. 그렇지 않나요, 이 첨사?”

순간 이풍의 굵은 눈썹이 꿈틀거렸다. 만난 지 5분도 안 됐지만 하나는 알겠다.

이풍이 홍진을 싫어한다는 것.

그거 하나만으로도 예의를 갖출 만한 상대다. 나는 공손히 포권을 취했다.

“태원진가의 진태경이라고 합니다.”

“위명은 익히 들었소. 산서 무림에 큰 신성이 떠올랐다고.”

“신성이라뇨, 과찬의 말씀이십니다.”

이풍이 진지한 얼굴로 고개를 저었다.

“아니오. 소문이라는 것이 왕왕 과장되기 마련인데, 내 오늘 진 소협을 보니 모두 사실임을 알겠소.”

오는 말이 고우면 가는 말도 고운 법.

나도 오는 길에 봤던 군사들 이야기를 꺼냈다.

“저야말로 군사들 수준이 상당히 뛰어나서 깜짝 놀랐습니다. 어떤 분이 훈련시켰는지 궁금했는데…… 역시는 역시네요.”

엄지를 척 치켜세워 주자 이풍의 입가에 웃음이 스친다.

이런 정상적이고 훈훈한 대화가 얼마 만인지, 감개가 무량할 지경이다.

“결례가 안 된다면 다른 분들도 소개해 주시겠소?”

“어이구, 그럼요. 이쪽은…….”

“안녕하십니까! 존경하는 무림의 선배님들과 불철주야 나라를 위해 힘쓰시는…….”

“…….”

대기업 면접이야, 뭐야.

호시탐탐 기회만 엿보고 있던 산서오문의 후기지수들이 앞다투어 과장된 자기소개와 아부를 한바탕 쏟아 내자 남은 한 사람에게 시선이 쏠렸다.

“그래, 거기 계신 후배님은 어디에서 온 누구신가?”

한껏 선배뽕에 취한 공일혁의 질문에 청풍이 눈을 깜빡였다.

“저요?”

“그럼 자네 말고 누가 있나?”

“하나, 둘, 셋, 넷…… 저 말고도 많은데요.”

공일혁의 이마에 핏대가 섰다.

“그거 말고! 아직 소개 안 한 건 자네뿐이잖아!”

“아하, 그렇군요. 후배라고 하시기에 제가 아닌 줄 알았어요.”

“어허, 원래 무림은 동도! 다 선후배지간인 걸 왜 모르는가!”

나 같았으면 잔뜩 비꼬았겠지만, 청풍은 역시 청풍.

일반인과는 클라스가 다르다.

“우와, 저 후배 처음 해 봐요! 잘 부탁드립니다!”

“……아니, 뭐 이런 놈이.”

가끔은 적당히 때 묻은 어른들보다 순수한 어린아이가 훨씬 대하기 어렵다. 청풍이 해맑은 웃음과 함께 입을 열었다.

“저는 산서에 살고 있는 청풍이라고 합니다.”

말문이 막혔던 공일혁이 그제야 정신을 차리고 더듬더듬 물었다.

“커, 커험. 그럼 자네도 산서오문의 후기지수겠군.”

“어? 아닌데요?”

“아니라고?”

“네. 전 하남에서 왔는데.”

“방금은 산서 사람이라며?”

“산서에 살고 있으니 산서 사람이지요. 헤헤.”

“그…… 후우우.”

공일혁의 이마에 골이 패었다. 당장이라도 주먹을 휘두르고 싶은데, 자리가 자리인 만큼 참는 기색이 역력했다.

“좋아, 그럼 하남 어느 문파 출신인가? 철혈문? 오호검문?”

“거기가 어디예요?”

“하남 출신이라면서 철혈문과 오호검문을 모르는 게 말이 되나? 응? 그럼 자네가 소림사 출신이라도 돼?”

“아, 하남에서는 보름 정도 머무르다가 산서로 넘어와서 잘 모릅니다.”

“하남 출신이라며?”

“하남에서 온 건 맞는데, 그전에는 섬서에…….”

“야, 이 새끼야! 차라리 그냥 천하가 네 고향이라고 해라!”

결국 폭발한 공일혁이 고함과 함께 청풍의 멱살을 붙잡았다. 아니, 붙잡으려던 찰나였다.

덥석.

너무나 간단하게 잡혀 버린 손목. 공일혁이 헛웃음을 흘렸다.

“허, 이놈 봐라. 한 수 재간은 있다, 이거지?”

“어어, 본능적으로 그만. 죄송합니다, 선배님.”

“본능적으로? 죄송해?”

울상이 된 얼굴로 사과하는 청풍을 보며 공일혁이 피식 웃었다.

“아니다. 놓을 것 없다. 사과할 것도 없고.”

“정말요?”

“그래, 그 대신 만용의 대가는 톡톡히 치러야겠지?”

“예? 그게 무슨.”

“이제부터 알게 될 거다.”

내가 끼어든 것은 바로 그 순간이었다. 몸을 날려 청풍의 앞을 막아선 나를, 공일혁이 건조한 눈빛으로 응시했다.

“비키시게, 후배님.”

“잠시 실례하겠습니다. 선배님.”

“실례라…… 본문의 행사에 태원진가가 반하겠다는 뜻으로 받아들이면 되겠나?”

나는 태연하게 대답했다.

“천만에요. 그저 문제가 커지는 걸 막고 싶을 뿐입니다.”

“문제? 무슨 문제?”

“곧 전하께서 오시지 않습니까? 여긴 보는 눈도 많고요.”

“보는 눈이라. 도지휘동지, 어떻게 생각하십니까?”

공일혁의 등 뒤로 빙긋 웃는 홍진의 얼굴이 보였다. 간드러진 목소리가 뒤를 잇는다.

“글쎄요, 제 생각엔 별문제 없을 것 같은데요?”

이풍이 즉시 반발했다.

“이곳은 대전입니다. 작은 소동도 용납할 수 없습니다.”

“이 첨사, 용납이라는 말은 듣기 거북하네? 누가 들으면 내 상관이라도 되는 줄 알겠어.”

“도지휘동지!”

“왜요, 도지휘첨사?”

홍진의 말이 떨어지기가 무섭게 종남삼수에 속한 다른 두 명이 슬그머니 이풍의 앞을 막아선다.

종남파라는 이름답게 각각 최소 초일류의 고수들. 이풍은 입술을 질끈 깨물더니 나를 보며 중얼거렸다.

“미안하오.”

공일혁이 득의양양하게 웃었다.

“자, 이제 어쩔 텐가?”

어쩌긴 뭘 어째. 어깨를 한번 으쓱하고 물러나자 공일혁의 웃음이 진해졌다.

“현명한 선택이야.”

“저는 문제가 커지는 걸 막고 싶었을 뿐입니다. 아시죠?”

“알다마다. 여기 있는 모두가 똑똑히 기억할 걸세.”

“그랬으면 좋겠네요.”

청풍은 멀뚱멀뚱 나를 쳐다봤다.

“은인, 혹시 제가 뭘 잘못했나요?”

내 대답보다 공일혁이 한발 빨랐다.

“뭐라? 잘못?”

찢어 죽일 듯한 눈빛이 청풍을 향했다.

“네가 지금 나와 종남파를 능멸하는 것이냐?”

“그게 아니고요. 저는 그저…….”

“그 입 닥치지 못할까!”

청풍의 얼굴 위로 복잡 미묘한 감정이 떠올랐다. 그리고 공혁일의 이성을 잃게 만들기에 충분한 한마디가 이어졌다.

“와, 저 누구한테 욕먹는 거 처음이에요. 신기하다.”

“이런 쳐 죽일……!”

후웅!

묵직한 파공성. 공혁일의 일권(一拳)이 눈부신 속도로 청풍의 옆구리를 향해 쏘아진 다음 순간이었다.

퍽, 우두둑.

“……!”

“……!”

소리 없는 경악 속, 한 사람이 고통으로 입을 딱 벌렸다.

으스러진 주먹과 팔뚝 살을 찢고 뛰어나온 뼈, 피투성이가 된 공혁일이 떨리는 목소리로 물었다.

“이, 이게 무슨. 도대체 어떤 권법…….”

그가 아니었다면 내가 물어봤을 거다. 이미 예상한 결과이기는 했지만, 이 정도일 줄이야.

청풍은 단 한 번 맞받아치는 것만으로 70레벨이 넘는 공일혁을 저항 불능으로 만들어 버렸다.

그리고…….

“권법이 아니었어.”

내 중얼거림에 청풍이 금방이라도 토할 것 같은 얼굴로 대답했다.

“은인 말씀이 맞아요. 권법이 아니라 태을미리장(太乙迷離掌)이라는 장법이에요. 그런데 선배님, 피가 너무 나요. 피 냄새 때문에 속 울렁거려요. 우욱!”

이런 미친놈.

공일혁을 내팽개치고 헛구역질을 시작하는 녀석을 보며 헛웃음을 흘리던 그때였다.

“태, 태을미리장!”

이풍이 부릅뜬 눈으로 물었다.

“지금 태을미리장이라고 했소? 정말 틀림없소?”

“우욱, 네. 저희 할아버지께서 가르쳐 주셨어요.”

“호, 혹시 그분의 존함을 여쭤봐도 되겠소?”

“우욱, 매종학, 우웨에에엑!”

촤아아악!

나는 청풍이 곧 왕이 도착할 자리에 토를 했다는 사실에 놀랐지만, 이풍은 아닌 듯했다.

벼락을 맞은 것처럼 부들부들 떨던 그가 목소리를 쥐어짜 냈다.

“검성……!”
```

## Final English reading copy

```markdown
# Chapter 140

Gong Ilhyuk of the Three Hands of Zhongnan stared at the young man in front of him with a dubious expression.

*What is this guy?*

Jin Taekyung, the Sleeping Dragon of Shanxi. He was the driving force behind a whirlwind that had quietly spread his name as far as Shaanxi in the span of only a few months.

Gong Ilhyuk mulled over what Jin Taekyung had said.

*“The Reign…” What was it?*

It definitely seemed as though he had been about to say something before stopping himself.

Unlike his enthusiastic reaction when he first heard the name of the Zhongnan Sect, he now looked completely deflated and let out one deep sigh after another.

“Whew.”

“…What’s with the sighing?”

“It’s nothing. Really.”

“What do you mean, nothing? Go on and finish what you were saying.”

Gong Ilhyuk was beginning to feel irritated. What kind of sect was his? It was none other than the famous Zhongnan Sect.

It was one of the great pillars of Murim, a sect that had proudly earned its place among the Nine Sects and One Gang on the strength of centuries of history and deeply rooted martial traditions.

And yet…

*Can’t he at least be grateful that I acknowledged him? Why is he sighing?*

No matter how successful the Jin Family of Taiyuan was, it was still merely a family from the frontier.

Compared to the Zhongnan Sect, one of the Nine Sects and One Gang, it was like a firefly before the sun. In terms of both background and personal fame, Jin Taekyung was a hopelessly insignificant greenhorn.

*What an arrogant bastard.*

Gong Ilhyuk had lived his entire life with pride in being a disciple of the Zhongnan Sect. It was only natural that he felt offended.

The other two men known alongside him as the Three Hands of Zhongnan were also looking at Jin Taekyung with displeasure.

“Ahem.”

“Young friend, you have a habit of stopping halfway when you speak.”

As the atmosphere grew increasingly unpleasant, Jin Taekyung waved his hand.

“No, it’s not like that. I just misunderstood something on my own.”

Gong Ilhyuk opened his mouth, deliberately adopting a generous tone.

“What did you misunderstand? Tell me. I’ll answer everything.”

“It’s really nothing…”

“Ah, just tell me!”

“Why are you shouting?”

Gong Ilhyuk took a deep breath.

He was almost forty years old. Yet here he was, getting worked up over a brat barely twenty.

For some reason, looking at that handsome face made his blood boil.

“It’s not that… Whew. Anyway, tell me.”

“Hmm.”

Jin Taekyung finally opened his mouth, as though he had no choice.

“Then may I ask you one thing?”

“Anything.”

“What is the name of the current chairman of the Zhongnan Sect—or rather, the Sect Leader?”

“Hm? You mean the Sect Leader’s name?”

“Yes.”

What kind of question was that? Gong Ilhyuk answered with a puzzled look.

“Gong Iljung.”

“Ah. Yes.”

Jin Taekyung’s response was so indifferent that it was as though he had no idea who that was.

The veins on the foreheads of all three men began to bulge.

“Have you never heard the Sect Leader’s name?”

Jin Taekyung scratched the back of his head.

“I think I have. Or maybe not…”

“…Then what about the title Wind-and-Cloud Sword Lord?”

“Wind-and-Cloud Sword Lord Gong Iljung. Wind-and-Cloud Sword Lord Gong Iljung… Hmm. I’m not sure.”

It was beyond absurd.

The Sect Leaders and Family Heads of the Nine Sects and One Gang and the Five Great Families were all renowned masters whose names were known throughout the world. No martial artist could possibly be unaware of them.

And yet this fellow, who was supposedly a member of the Jin Family of Taiyuan—not some half-baked martial artist—didn’t know the Sect Leader of the Zhongnan Sect.

He even called him by his given name, as though they were friends.

*Is this bastard making a mockery of the Zhongnan Sect?*

Gong Ilhyuk’s head was spinning from the shock when Jin Taekyung suddenly looked up at him.

“Oh? Now that I think about it, your names are similar. Gong Iljung, Gong Ilhyuk.”

At least he had some basic social awareness. Gong Ilhyuk’s irritation eased slightly.

“He’s a family elder.”

“Oh, a family elder! Then are you two…?”

“He’s my father’s cousin.”

“Your father’s cousin!”

Seeing Jin Taekyung’s eyes widen, Gong Ilhyuk straightened his shoulders.

It wasn’t just anyone. He was the Wind-and-Cloud Sword Lord. Being related to the Sect Leader of the Zhongnan Sect was an immense honor.

“Ahem. Don’t spread it around too much. If this became widely known, people’s attitudes toward me would change.”

In reality, Gong Ilhyuk wanted this fact to become known more than anyone.

He had enjoyed all kinds of benefits by putting the Wind-and-Cloud Sword Lord’s name out front: superior martial arts, elixirs, and even the title of Three Hands of Zhongnan.

If he continued advancing at this rate, it was only a matter of time before he seized an important position within the Zhongnan Sect.

“You understand what I mean, right? If you absolutely have to tell someone, just tell a few close friends…”

Jin Taekyung waved his hand.

“No way. I’d never tell anyone. It would obviously hurt Great Hero Gong’s reputation. People would say, ‘He’s a guy who climbed this high by relying on connections.’ Oops. Sorry. Anyway, that kind of rumor would be troublesome, wouldn’t it?”

Gong Ilhyuk gave a dry cough. Even he had to admit that the boy wasn’t entirely wrong.

“Ahem. It’s not as though it would hurt me that much. I only meant that there might be people who are curious about me…”

“People curious about you? I don’t have a single friend, so there’s no one I could tell.”

“…Your eldest brother, the Lesser Family Head of the Jin Family, might be curious. Or Young Hero Heaven Shaking Sword.”

“Oh, you don’t know much about my family situation. My eldest brother is incredibly busy right now. My second brother isn’t interested in much besides martial arts.”

“…Really?”

“Yes.”

There was nothing more to say after that.

As Gong Ilhyuk continued giving irritated coughs, Jin Taekyung smiled brightly.

“And what good would it do to tell anyone? If he’s only your father’s cousin, you’re practically strangers. I thought you two were father and son or something.”

“……!”

* * *

There was nothing more exhilarating than screwing someone over while smiling.

Especially when it was someone who acted arrogant. If I managed to get one over on them properly, the rush doubled.

*Ah. I think I could get addicted to this.*

Were they called the Three Hands of Zhongnan?

I hadn’t liked them from the moment I met them. Not their gazes, which seemed to look down on everyone, nor their swaggering attitude as members of a great sect.

*So it really is different from the novel.*

When I was in high school, becoming a disciple of the Zhongnan Sect had been one of my dreams.

As expected, reality was a cesspool.

I held back my laughter as I watched Gong Ilhyuk trembling with rage.

*What a cute bastard. He’s so much fun to tease.*

I wanted to keep going, but this was probably enough. If the Jin Family of Taiyuan was a local player, these people were national-level.

There was nothing to gain from picking a fight with them.

Fortunately, a voice suddenly cut in and lightened the atmosphere.

“Aren’t you gentlemen monopolizing the conversation a little? The other guests must be lonely. You haven’t even finished introducing yourselves.”

I got goose bumps once at the nasal, lilting voice.

Then I got them a second time when the pretty middle-aged man looked at me and winked.

“I haven’t introduced myself yet, have I? I’m Hong Jin, the Deputy Military Commissioner of Shanxi Province.”

“Deputy Military Commissioner… what?”

“The Deputy Military Commissioner. Ah, you’re a martial artist, so I suppose this is your first time hearing of the office?”

“Yes.”

*I’d heard of “Comrade Chairman,” but “Comrade Deputy Military Commissioner” was a new one.*

Hong Jin giggled as he looked at me blinking.

Good heavens. A middle-aged man was giggling.

“Why that expression? Did something bad happen?”

“…No. I’m just so happy.”

“Happy? Ho ho ho, you’re adorable. Don’t you agree, Assistant Commissioner Li?”

*He called me cute. Fuck, that bastard called me cute.*

I was barely holding back my nausea when the man I had seen only briefly earlier greeted me in a blunt voice.

“I am Li Feng, Assistant Military Commissioner of Shanxi Province. I oversee the training of the soldiers under the Shanxi Provincial Office.”

“And he’s my direct subordinate. Isn’t that right, Assistant Commissioner Li?”

Li Feng’s thick eyebrow twitched.

We had known each other for less than five minutes, but I already knew one thing.

Li Feng hated Hong Jin.

That alone made him someone worth treating with courtesy. I performed a fist-and-palm salute.

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

“I have heard your reputation. A great new star has risen over the Shanxi martial world.”

“A new star? You flatter me.”

Li Feng shook his head with a serious expression.

“No. Rumors are often exaggerated, but after seeing Young Hero Jin today, I can tell they were all true.”

Kind words deserved kind words in return.

I brought up the soldiers I had seen on the way here.

“I was surprised by how skilled the soldiers were. I wondered who had trained them, but I suppose it was only natural that it would be you.”

I gave him a firm thumbs-up, and a smile flickered across Li Feng’s lips.

It had been so long since I’d had a normal, pleasant conversation that I was almost moved.

“If it isn’t discourteous, could you introduce the other guests as well?”

“Of course. This is…”

“Greetings! To the respected Seniors of Murim and those who toil day and night for the sake of the nation…”

“……”

What was this, an interview at a conglomerate?

The young prodigies of the Five Gates of Shanxi, who had been waiting for an opportunity, rushed to give exaggerated introductions and shower everyone with flattery.

That left only one person.

“All right. Junior, where are you from, and who are you?”

At Gong Ilhyuk’s question, delivered with all the smugness of someone high on his seniority, Cheongpung blinked.

“Me?”

“Who else would I mean?”

“One, two, three, four… There are lots of people besides me.”

The veins on Gong Ilhyuk’s forehead bulged.

“Not that! You’re the only one who hasn’t introduced himself!”

“Oh, I see. You called me a junior, so I didn’t think you meant me.”

“Good heavens! In Murim, we’re all fellow practitioners! We’re all seniors and juniors to one another. How do you not know that?”

If it were me, I would have responded with heavy sarcasm.

But Cheongpung was Cheongpung.

He was in a different class from ordinary people.

“Wow, this is my first time being a junior! I look forward to working with you!”

“…What kind of person is this?”

Sometimes, a pure child was much harder to deal with than an adult who had been properly tainted by the world.

Cheongpung spoke with a bright smile.

“My name is Cheongpung, and I live in Shanxi.”

Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question.

“Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.”

“Hm? No.”

“You’re not?”

“No. I came from Henan.”

“You just said you were from Shanxi.”

“I live in Shanxi, so I’m from Shanxi. Hehe.”

“Then… whew.”

A furrow appeared in Gong Ilhyuk’s forehead.

He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back.

“All right, then. Which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?”

“Where are those?”

“You’re from Henan, but you don’t know the Iron Blood Sect or the Five Tigers Sword Sect? Does that make any sense? Hm? Then are you from Shaolin?”

“Oh, I stayed in Henan for about half a month before moving to Shanxi, so I don’t know much about it.”

“You said you were from Henan?”

“It’s true that I came from Henan, but before that I was in Shaanxi…”

“You little bastard! Then just say the whole world is your hometown!”

At last, Gong Ilhyuk exploded. He shouted as he grabbed Cheongpung by the collar—or tried to.

Snag.

His wrist was caught with absurd ease.

Gong Ilhyuk let out a hollow laugh.

“Well, look at you. You know at least one trick, huh?”

“Ah, I just reacted on instinct. I’m sorry, Senior.”

“On instinct? And you’re apologizing?”

Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh.

“Never mind. You don’t have to let go. There’s no need to apologize, either.”

“Really?”

“Yes. But you’ll pay dearly for your reckless bravado.”

“What? What does that mean?”

“You’ll find out soon enough.”

I stepped in at that exact moment.

I threw myself in front of Cheongpung, and Gong Ilhyuk looked at me with dry eyes.

“Move aside, Junior.”

“Pardon me, Senior.”

“Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?”

I answered calmly.

“Not at all. I only want to prevent this from becoming a bigger problem.”

“A problem? What problem?”

“His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.”

“Plenty of eyes. Deputy Military Commissioner, what do you think?”

I could see Hong Jin smiling behind Gong Ilhyuk.

His delicate voice followed.

“Well, I don’t think it will be much of a problem.”

Li Feng immediately objected.

“This is the grand hall. We cannot tolerate even a minor disturbance.”

“Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.”

“Deputy Military Commissioner!”

“Why, Assistant Military Commissioner?”

The instant Hong Jin finished speaking, the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng.

As befitted members of the Zhongnan Sect, both were at least advanced First Rate masters.

Li Feng bit down hard on his lip, then muttered to me,

“I’m sorry.”

Gong Ilhyuk smiled triumphantly.

“Well? What are you going to do now?”

What was I supposed to do?

I shrugged once and stepped back. Gong Ilhyuk’s smile deepened.

“A wise choice.”

“I only wanted to prevent the problem from getting bigger. You understand, right?”

“Of course. Everyone here will remember it clearly.”

“I hope so.”

Cheongpung stared blankly at me.

“Benefactor, did I do something wrong?”

Gong Ilhyuk was faster than I was with his response.

“What? Wrong?”

His gaze turned murderous as he glared at Cheongpung.

“Are you insulting me and the Zhongnan Sect right now?”

“That’s not it. I was just…”

“Can’t you shut that mouth of yours?”

A complicated, subtle expression appeared on Cheongpung’s face.

Then he said the one thing more than enough to make Gong Ilhyuk lose his reason.

“Wow, this is the first time anyone’s ever sworn at me. How fascinating.”

“You goddamn bastard…!”

Whoosh!

A heavy sound split the air.

Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed.

Then—

Crack. Crunch.

“……!”

“……!”

Amid the silent shock, one man opened his mouth wide in pain.

His fist had been crushed. Bone jutted through the torn flesh of his forearm, and blood covered Gong Ilhyuk as he asked in a trembling voice,

“Wh-what is this? What kind of fist technique…?”

If he hadn’t asked, I would have asked the same thing.

I had expected this result, but not to this extent.

With a single counter, Cheongpung had rendered Gong Ilhyuk, a Level 70-plus master, completely helpless.

And then…

“It wasn’t a fist technique.”

At my mutter, Cheongpung answered with a face that looked ready to vomit.

“Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!”

What a lunatic.

I gave a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began dry heaving.

That was when—

“Ta-Taeeul Miri Palm!”

Li Feng asked with his eyes wide.

“Did you just say Taeeul Miri Palm? Are you certain?”

“Urk, yes. My grandfather taught me.”

“M-May I ask his name?”

“Mae Jonghak, urk—urgh!”

Splash!

I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed.

He trembled as though he had been struck by lightning, then squeezed out a single word.

“Sword Saint…”
```
