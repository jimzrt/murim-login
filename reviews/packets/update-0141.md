<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0141.txt",
      "sha256": "0d0196c2056dc8eecc8d6ea2a18df05f2e8e3142e38d5a391f301d9fc08836b8",
      "bytes": 14829
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "21a166172e312e718e589f32cd7c1c2bbe7f35a7bddf44fd498095aa7c414a6f",
      "bytes": 2533
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ffbd2752e399ea7b05ee37915e1c80573f3ef974bf775a1c8292d3aa73fd5727",
      "bytes": 29516
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b79f94666958450ec44b4882947e52c861885ca61c641c005bd1d7402be91fc9",
      "bytes": 830
    },
    {
      "path": "characters/Gong Ilhyuk.md",
      "sha256": "ddc00963a8dfceaa93351ac545ca7b974a5d5ad9247fa1b8e61415dbda75871f",
      "bytes": 614
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "7dbf8542c27f8996b81ee6305467908ed54f9777ea459af598905ed7255c213e",
      "bytes": 682
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "f4145ef258573daa94949debf33ee283e860e92581eadffbd5ed982f957193d6",
      "bytes": 1511
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "901831f8cc796ae568dfe3ddad9aecd0570c4fad6e6f2efd6331fbaf8ef507cb",
      "bytes": 648
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "16883ed0b43ebff12628a15da9d13942c6d370363cccd6a1ad463bc928c47dde",
      "bytes": 407
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4b728a22b0d7f4b192a8223a0e93a6343e6dfdad1588dc15d86b299b7c1c2338",
      "bytes": 24902
    }
  ],
  "estimated_tokens": 24294
}
-->

# Durable State Update — Chapter 141

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 141. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 141. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 141,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 141,
    "continuity_sources": [141],
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
    "The Jin Family group is attending the City Lord's luncheon at the Shanxi Provincial Office, where His Highness is expected to arrive soon.",
    "Hong Jin is the Level 22 Deputy Military Commissioner of Shanxi Province and Li Feng's direct superior.",
    "Li Feng is the Assistant Military Commissioner of Shanxi Province, a former Huashan lay disciple who trains the Provincial Office's soldiers.",
    "Gong Ilhyuk and two unnamed martial artists are the Three Hands of Zhongnan; Ilhyuk is nearly forty and above Level 70.",
    "Gong Iljung is the current Sect Leader of the Zhongnan Sect and the Wind-and-Cloud Sword Lord; he is Gong Ilhyuk's father's cousin.",
    "Gong Ilhyuk benefits from his relationship to Gong Iljung and takes pride in being a Zhongnan disciple.",
    "Cheongpung lives in Shanxi, previously stayed in Henan, and came there after being in Shaanxi.",
    "Cheongpung's grandfather is Mae Jonghak, the Sword Saint, who taught him the Taeeul Miri Palm.",
    "Cheongpung defeated Gong Ilhyuk with one counter using the Taeeul Miri Palm, crushing his attacking arm.",
    "Cheongpung becomes nauseated by the smell of blood and vomits after the fight.",
    "Taekyung intervened to prevent the confrontation from becoming a public disturbance, then stepped back when the other two Three Hands blocked Li Feng.",
    "Taekyung's unfinished reference beginning with 군림 remains unclear."
  ],
  "continuity_sources": [
    139,
    140
  ],
  "open_questions": [
    "What conflict involving the Assistant Military Commissioner, Huashan, and an insult preceded Taekyung's arrival at the luncheon?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What was Taekyung about to say after recognizing the Zhongnan Sect from the novel?"
  ],
  "safe_through": 140,
  "temporary_decisions": [
    "Render 전하 as “His Highness” when used as the formal royal address.",
    "Render 왕 as “king” when Cheongpung uses it literally, while preserving the official correction to “His Highness.”",
    "Render 초일류 as “advanced First Rate.”",
    "Render 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord.”",
    "Render 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in this exchange."
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
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |

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
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검법     | **sword technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 극양                        | **Extreme Yang**      |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 140
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather Mae Jonghak, the Sword Saint, in the mountains from age five; Mae Jonghak taught him the Taeeul Miri Palm; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Gong Ilhyuk.md

# Gong Ilhyuk (공일혁)

- **Safe through:** Chapter 140
- **Aliases:** None
- **Role:** The third member of the Three Hands of Zhongnan and a Zhongnan Sect martial artist from Shaanxi
- **Personality:** Sharp-tongued, mocking, and openly antagonistic toward Li Feng
- **Voice:** Casual, taunting, and deliberately provocative
- **Relationships:** Member of the Zhongnan Sect's Three Hands; Gong Iljung, the Sect Leader and Wind-and-Cloud Sword Lord, is his father's cousin; involved in a ten-year-old humiliating martial grievance with Li Feng

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 140
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province attending the City Lord's luncheon; he interrupts a tense exchange and greets Jin Taekyung as a young hero of the Jin Family of Taiyuan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 139
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 140
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; bears a humiliating martial grievance involving Gong Ilhyuk

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 140
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

## Korean source

```text
＃141화



나는 며칠 전 진무경에게 들었던 말을 떠올렸다.

‘일신(一神), 삼성(三星), 십왕(十王).’

이미 전설이 되어 버린 위대한 무인들.

순서로 따지자면 검성 매종학은 천하를 통틀어 다섯 손가락 안에 드는 초절정 고수라는 말이 된다.

‘이제는 하다 하다 검성까지 나오는구나.’

진무경이 말하길, 화왕(火王)은 나흘 밤낮 동안 천 명의 마교도를 잡아 죽이고 십왕에 올랐다고 했다.

그렇다면 그보다 앞줄에 이름에 올린 검성은 어느 정도일까?

‘어떻게 된 게 갈수록 괴물만 튀어나오냐.’

기가 찼지만 청풍을 보니 한편으로는 고개가 끄덕여졌다.

콩 심은 데에서 콩 나는 법. 괴물이 괴물을 키운 거다.

‘저런 재능충이 쉽게 나올 리가 없지.’

청풍은 의심할 여지가 없는 절정 고수다.

그의 나이 이제 겨우 스물. 검성이라는 엄청난 고수의 지도 아래서 자랐다면 충분히 이해가 된다.

“우욱, 우웨에엑!”

……살짝 이해가 안 되려고 하네. 저런 놈이 어떻게 절정 고수가 된 거지?

나는 계속 구역질을 해 대는 청풍에게 물었다.

“괜찮아요?”

“저는 괜찮, 우욱!”

“안 괜찮으시구나.”

“그보다 선배님이 많이 다치신 것 같은데, 우웩!”

“선배님은 무슨. 괜찮아요. 저 정도는 침 바르면 다 나아.”

“정말요?”

당연히 아니지.

나는 청풍의 등을 두드려 주며 흘끗 주위를 둘러봤다. 홍진을 제외한 모두가 눈을 부릅뜨고 이쪽을 바라보고 있었다.

“거, 검성 매종학? 내가 아는 그 검성?”

“저 덜떨어진 놈이 검성의 손자라고?”

“도대체 이게 무슨…….”

그중에서도 유난히 눈에 띄는 것은 공일혁의 반응이었다. 놈은 고통도 잊은 채 멍하니 청풍을 바라보다가 버럭 소리쳤다.

“헛소리! 검성이 은거한 지 삼십 년이 넘었다! 어찌 네놈 따위가 검성의 후인을 자처하느냐!”

“저어, 말씀 중에 죄송한데요.”

나는 턱을 긁적이며 말을 이었다.

“우선 지혈부터 하시는 게 어떨까요. 피 엄청 많이 나는데.”

“…….”

공일혁의 얼굴이 벌겋게 달아올랐다. 본인도 부끄럽긴 할 거다. 한 방에 팔이 박살 난 주제에 네놈 따위를 운운했으니.

“큭, 내가 방심만 안 했어도…….”

“그럼 상처 나으시는 대로 재대결 추진해 볼까요? 저희 집 연무장 빌려 드릴 수 있는데.”

백번 싸워도 백번 질 것이 뻔하다. 그 정도로 두 사람의 격차는 확연했다.

그 증거로 막상 판을 깔아 주자 공일혁은 꿀 먹은 벙어리가 되어 입을 다물었다.

“지혈부터 하세요. 지혈부터.”

“……네놈.”

공일혁이 살벌한 눈빛으로 나를 노려본다.

이제야 내가 자신을 싫어한다는 걸 눈치챈 모양인데, 뭐 딱히 위협은 느껴지지 않는다.

‘말릴 때 그만두든가.’

괜히 오늘 일이 알려져 봤자 손해 보는 건 저쪽이다. 무려 검성의 손자와 엮였으니 오촌 당숙이라는 종남파 장문인 입장에서도 이게 달가운 일은 아닐 것이다.

반면에 나는 이 일의 당사자도 아닐뿐더러, 뜻밖의 황금 인맥을 얻었고.

‘내가 인마, 어? 검성 손자한테 빙당호로도 주고, 온천도 가고, 어? 다 했어, 이 새끼야.’

빙당 코인이 이렇게 떡상 하는구나.

내심 흐뭇하게 웃고 있을 때, 지혈을 끝마친 공일혁이 비웃었다.

“생각해 보니 웃기는구나. 내 알기로는 검성에게는 자식이 없는데, 어찌 장성한 손자가 있을 수 있단 말이냐?”

막 헛구역질을 멈춘 청풍이 고개를 갸우뚱했다.

“아닌데. 저 할아버지 손자 맞는데요.”

“검성이 무공에 평생을 매진했다는 것은 천하가 아는 사실, 네놈이 지금 거짓을 고하고 있는 게 분명하다!”

“아닌데. 진짜 아닌데.”

청풍은 울상이 된 얼굴로 말을 이었다.

“저 진짜 우리 할아버지 손자 맞아요. 이십 년 전에 두루미가 데려다줬어요.”

“……?”

“……?”

시벌, 이건 또 무슨 소리여.

사람들의 시선이 쏠리자 청풍이 혼란스러운 표정으로 나를 돌아봤다.

“은인, 제가 잘못 알고 있는 거예요?”

“……도대체 뭘 알고 계신 거예요?”

“두루미가 아기 데려다주는 거요. 원래 아기는 하늘이 점지해 주는 거라서 때가 되면 두루미가 데려다준다고 했는데.”

“누가 그래요?”

“할아버지가요.”

“아.”

딱 스토리 나온다. 성 씨부터 다른 걸 보니 검성이 어디서 입양해 온 게 분명한데…….

기억도 안 나는 어린 시절부터 산에서 할아버지와 단둘이 자랐다는 청풍이다.

무슨 말을 해도 그냥 그렇구나, 하고 받아들였겠지.

“두루미가 데려다주는 거 아니에요? 그럼 저 우리 할아버지 손자 아닌 거예요?”

“아, 그게 그러니까…….”

나는 무거운 마음으로 말을 이었다. 청풍의 나이 스물, 산에서 내려온 이상 하나씩 세상을 알아 갈 때가 됐다.

“아이가 나오려면 총 세 단계가 있어요. 배란, 수정, 착상. 한 번 해 보세요.”

“은인한테요?”

“그걸 왜 나한테 해요. 미쳤습니까? 소리 내서 따라 해 보라고요.”

“네. 배란, 수정, 착상…….”

그러나 야심 차게 시작한 성교육은 시작과 동시에 막을 내려야 했다.

“이 핏덩이 놈들이! 감히 무림의 대선배를 앞에 두고 뭣들 하는 짓이냐!”

으르렁거리는 목소리의 주인공은 당연하게도 공일혁이었다.

종남삼수라 쓰고 따까리라고 읽는 다른 두 명의 도움을 받아 부목까지 댄 그가 우리를 향해 눈을 부라렸다.

“변방 촌놈과 힘만 믿고 까부는 얼간이가 대 종남파의 제자를 무시해?”

청풍이 눈을 동그랗게 떴다.

“제가 얼간이인가요?”

“그럴걸요.”

“그럼 은인이 변방 촌놈이네요?”

“알려 줘서 되게 고맙네요.”

나는 한숨을 푹 내쉬었다. 나이도 먹을 만큼 먹은 양반이 아직도 상황 파악이 안 되는 모양이다. 종남파라는 배경과 오촌 당숙에 대한 믿음이 너무 강해서 그런가?

“거, 우리 선배님 주둥이가 참 방정이시네.”

“뭐라?”

“나야 그렇다 치고, 여기 이 친구가 한 말이 사실이면 어쩌시려고?”

“사실이라, 그랬다면 이풍이 못 알아봤을 리 없지.”

이풍? 이풍이 여기서 왜 나와?

나는 의문을 담아 이풍을 바라봤다. 귀신이라도 본 것처럼 딱딱하게 굳어 있던 그가 입술을 뗐다.

“나는 화산파의 속가제자요. 십 년 전까지만 해도 본산에 있었지.”

공일혁이 이죽거리는 얼굴로 덧붙였다.

“저 친구가 속가 중에서는 제법 잘나갔거든. 본문과의 친선 비무에서 나한테 패배하기 전까지는 말이야, 안 그런가?”

“맞아. 비무를 위해 종남파에서 이틀을 묵었는데 뭔가를 잘못 먹고 심하게 앓았지.”

“또 그 얘기군. 질리지도 않나?”

“매번 생각해도 공교로운 사실 아닌가. 나를 포함해 자네와 비무가 예정된 자들만 그런 일을 겪었다는 게 말일세.”

“……그래서, 아직도 패배를 인정하지 못하겠나?”

“아니, 오래전에 인정했네. 오히려 자네 덕분에 무림이 어떤 곳인지 알게 됐으니 수업료로는 값싸게 먹힌 거지.”

담담한 말투에 공일혁의 눈썹이 꿈틀거렸다.

“대인배 흉내는 그쯤하고 사실대로 대답하게. 저 얼간이를 화산에서 본 적이 있나?”

“그전에 하나만 묻지. 아직도 내가 화산을 떠난 이유가 자네 때문이라고 생각하나?”

“물론. 비무가 끝나고 두 달도 채 되기 전에 화산을 뛰쳐나간 주제에 무슨 변명을 하고 싶은 건가?”

“한동안 실의에 빠져 있던 건 사실이지만…… 틀렸어.”

고개를 저은 이풍이 천천히 말을 이었다.

“그날 이후 달포쯤 지났나? 사부님께서 갑자기 갈 곳이 있다고 하시더군. 따라간 곳에는 장문인을 비롯한 본문의 수뇌부들이 모두 모여 있었네.”

“속가제자를 위해 위로연이라도 베풀었나? 화산파, 생각보다 인심이 좋은 곳이었군그래.”

“인심이 좋은 건 사실이지. 나 같은 실패자를 태사부(太師父)를 뵈러 가는 중요한 자리에 끼워 줬으니까.”

공일혁의 눈이 가늘어졌다.

“태사부라면, 혹시?”

“본문의 태사부는 한 분뿐일세. 검성 매종학. 모두가 아는 그분이지.”

곳곳에서 탄성이 흘러나왔다. 반면 공일혁의 얼굴에는 점점 불안함이 번졌다.

“말도 안 돼. 검성은 오랫동안 모습을 드러내지 않았다고 들었는데…….”

“사실이야. 다만 그분은 여전히 화산에 남아 계셨네. 워낙 깊이 은거하시는 바람에 찾지 못했을 뿐.”

“그, 그래서?”

“화산을 이 잡듯이 뒤졌지. 열 개의 진법을 깨트리고 난 후에야 그분의 거처에 다다를 수 있었네. 내가 그곳에서 뭘 봤는지 짐작이 가나?”

이 자리에 있는 모두가 짐작할 수 있었다. 이풍의 시선이 청풍의 얼굴에 못 박혀 있었기 때문이다.

“귀여운 어린아이였네. 또래보다 훨씬 작은 체구로 열심히 검을 휘두르는데…… 아무도 웃지 못했지. 고작 열 살에 매화검법(梅花劍法)을 펼치는 괴물을 보고 누가 웃을 수 있었겠나?”

“……!”

“……!”

사람들 사이로 소리 없는 경악이 번졌다. 공일혁이 더듬더듬 입을 열었다.

“그건, 그건 말도 안 돼. 내가 알기로 매화검법은 최소 일류는 되어야…….”

“무림에서는 간혹 상상치도 못한 일들이 일어나더군. 친선 비무에서 수작을 부리는 것 따위는 아무것도 아니야.”

이풍은 자조 섞인 웃음을 지었다.

“한 달이 넘게 면벽 수련을 하고 깨달았지. 이곳에 남아 있을 이유가 없다는 것을. 그게 내가 화산파를 떠난 이유일세. 어때, 재밌지 않나?”

이풍이 들려준 이야기의 여파는 강렬했다. 나를 포함한 모두가 말없이 청풍을 바라봤다.

문득 지난 밤 홍화 객잔에서 그와 나눴던 대화가 떠오른다.



‘제가 열 살 때였는데, 어느 날 수십 명이 우르르 찾아와서 행패를 부리더군요. 할아버지께서 산에 불 질러 버리기 전에 꺼지라고 소리치시던 기억이 나요.’

‘아, 그래서 계속 거처를 옮기시는……?’

‘네, 다행히 산이 넓어서 십 년째 잘 피해 다니고 계세요.’



그때까지만 해도 몰랐다. 십 년 전 찾아와서 행패를 부렸다던 사람들이 화산파의 수뇌부고, 검성 매종학이 청풍의 할아버지였을 줄은.

행패를 부렸다는 것도 어린 청풍의 시선에서나 그렇지, 실상은 많이 달랐을 것이다.

‘검성한테 누가 행패를 부려. 죽기 딱 좋지.’

사문에 불을 지르겠다고 협박한 검성도 보통이 아니다.

어쨌든 화산이 진짜 화산(火山)이 될 뻔한 그 날, 이풍은 어린 시절의 청풍을 만났고 그 천재성에 절망했던 것이 분명했다.

‘그럴 만도 하지. 열 살에 일류라니.’

약관을 넘겨도 일류에 다다르지 못하는 이들이 부지기수다.

당장 이 자리에 있는 산서오문의 후기지수 중 두 명 또한 아직도 일류 고수라고 하기에는 부족하다.

그런데 고작 열 살에 그 경지를 이룩했다니.

‘진무경이라면 가능했을까?’

그런 의문이 떠오른 순간, 공일혁이 발작처럼 외쳤다.

“증거! 저자가 그 어린아이라는 증거는?”

어떻게든 잘 보이려고 애쓰던 산서오문의 후기지수들과 흥미진진하게 구경하던 홍진, 심지어는 종남삼수에 함께 속한 두 사람까지. 모두가 약속이라도 한 듯 눈살을 찌푸렸다.

“증거는 없네. 내 기억이 전부야.”

“그렇지. 십 년이면 강산도 변하는데, 자네의 그 알량한 기억력을 믿어야 하나?”

“아니, 사실 나도 확신이 서지 않네. 그 어린아이가 어떻게 장성했는지 말이야.”

침착하게 대꾸한 이풍이 돌연 검을 뽑았다.

스릉, 서늘한 한기를 뿌리는 검신을 들여다보던 그가 청풍에게 물었다.

“소협. 화산파의 무공을 얼마나 아시오?”

청풍이 얼떨떨한 표정으로 대꾸했다.

“어어, 저는 화산파가 아닌데요.”

“화산파가 아니다…….”

“네. 할아버지께서 익히면 좋다고 이것저것 알려 주신 것뿐이에요.”

“하면 묻겠소. 육합검, 매화검법, 상청검, 태을미리장, 낙화추영장, 산화무영수…… 이 중 얼마나 알고 있소?”

“전부요.”

“허허, 전부. 전부라.”

실소를 터트린 이풍이 들고 있던 검을 청풍에게 건넸다.

“매화검법을 펼쳐 볼 수 있겠소?”

“할아버지께서 무공은 보여 주지 말라고 하셨는데.”

“일 초식, 아니 일검이면 족하오.”

머뭇거리던 청풍이 검파를 잡았다.

“그럼 짧게 보여 드릴게요.”

말이 끝나기가 무섭게 변화가 일어났다.

스아아아아.

검기? 아니다. 청풍의 머리부터 발끝까지. 전신에서 유형화된 자줏빛 기운이 올올이 흘러나왔다.

그것은 가까이 있는 것만으로도 숨결을 태우는 극양의 공력이었다.

“자하신공(磁荷神功)……!”

이풍이 희열에 찬 탄성을 토해 낸 그때.

쉬익!

청풍의 검 끝이 아름다운 궤적을 그렸다.

마치 계절의 끝에서 낙화하는 매화처럼, 한 줄기 검기가 거대한 탁자를 반으로 갈랐다. 음식과 접시, 단단한 탁자까지.

“아…….”

나도 모르게 탄성이 흘러나왔다.

깨트리는 건 쉽다. 그러나 청풍의 검기는 너무나도 예리하고 깔끔했다. 다음 순간, 탁자가 무너지지 않았다면 베였다는 것을 눈치 못 챌 정도로.

쿠웅! 촤아아악!

두 동강 난 탁자가 무너짐과 동시에, 이풍이 지극히 공손한 자세로 포권을 취했다.

“화산파 속가제자 이풍, 청풍 사숙(師叔)께 인사 올립니다.”
```

## Final English reading copy

```markdown
# Chapter 141

I recalled something Jin Mukyung had told me a few days ago.

*One God, Three Saints, Ten Kings.*

Great martial artists who had already become legends.

Going by that order, Sword Saint Mae Jonghak had to be one of the top five Supreme Peak masters in the world.

*Now even the Sword Saint is showing up.*

Jin Mukyung had told me that the Fire King earned his place among the Ten Kings by hunting down and killing a thousand members of the Demonic Cult over four days and nights.

If that was what it took to earn a place among the Ten Kings, just how formidable was the Sword Saint, whose name ranked ahead of his?

*Why do nothing but monsters keep popping up?*

I was dumbfounded, but then I looked at Cheongpung and found myself nodding.

Beans grow where beans are planted. A monster had raised a monster.

*There’s no way a gifted freak like that could appear out of nowhere.*

Cheongpung was unquestionably a Peak master.

He was only twenty years old. If he had grown up under the guidance of a phenomenal master like the Sword Saint, it made perfect sense.

“Urk, uweeek!”

…Actually, it was starting to make less sense. How had someone like that become a Peak master?

I asked Cheongpung, who continued retching.

“Are you all right?”

“I’m all right, urk!”

“You’re clearly not all right.”

“More importantly, Senior looks badly hurt, ugh!”

“Don’t call me Senior. I’m fine. A little spit and this much will heal right up.”

“Really?”

Of course not.

I patted Cheongpung on the back and glanced around. Everyone except Hong Jin was staring at us with wide eyes.

“S-Sword Saint Mae Jonghak? The Sword Saint I know?”

“That idiot is the Sword Saint’s grandson?”

“What on earth is going on…?”

Gong Ilhyuk’s reaction stood out more than anyone else’s. He had apparently forgotten his pain and was staring blankly at Cheongpung before suddenly shouting.

“Nonsense! The Sword Saint has been in seclusion for more than thirty years! How dare a piece of trash like you claim to be the Sword Saint’s heir?”

“Excuse me for interrupting.”

I scratched my chin and continued.

“Why don’t you stop the bleeding first? You’re losing a lot of blood.”

“……”

Gong Ilhyuk’s face turned bright red. He had to be embarrassed. His arm had been shattered with a single blow, yet he was still calling someone else a piece of trash.

“Tch. If only I hadn’t let my guard down…”

“Then shall we arrange a rematch once you’ve recovered? I can lend you my family’s training hall.”

Even if they fought a hundred times, Gong Ilhyuk would lose all hundred. The difference between the two of them was that obvious.

The proof was that, now that I had actually offered him the chance, Gong Ilhyuk went silent as though he had swallowed honey.

“Stop the bleeding first. Stop the bleeding.”

“……You bastard.”

Gong Ilhyuk glared at me with murderous eyes.

It seemed he had finally realized that I disliked him, but I didn’t feel particularly threatened.

*You should’ve stopped when I told you to.*

If word of what happened today got out, they were the ones who would suffer. They had gotten entangled with the Sword Saint’s grandson, and even the Sect Leader of the Zhongnan Sect—Gong Ilhyuk’s father’s cousin—wouldn’t be happy about that.

Meanwhile, I wasn’t even directly involved. I had also gained an unexpected golden connection.

*Listen here, I gave the Sword Saint’s grandson candied hawthorn skewers[^1], took him to the hot springs, and did it all, okay? You bastard.*

So this was how the candied-hawthorn stock took off.

I was smiling inwardly when Gong Ilhyuk finished stopping the bleeding and sneered.

“Come to think of it, this is ridiculous. As far as I know, the Sword Saint had no children. How could he possibly have a grown grandson?”

Cheongpung, who had just stopped retching, tilted his head.

“That’s not true. I really am his grandson.”

“The entire world knows that the Sword Saint devoted his entire life to martial arts! You’re obviously lying!”

“No, I’m really not.”

Cheongpung continued with a miserable expression.

“I really am my grandfather’s grandson. A crane brought me to him twenty years ago.”

“……?”

“……?”

*What the fuck was that supposed to mean now?*

As everyone’s attention turned toward him, Cheongpung looked back at me with a confused expression.

“Benefactor, am I mistaken?”

“What exactly do you know?”

“About cranes bringing babies. Grandfather told me that babies are chosen by Heaven, and when the time comes, a crane delivers them.”

“Who told you that?”

“My grandfather.”

“Oh.”

The story practically wrote itself. Their surnames were different, so the Sword Saint had obviously adopted him from somewhere…

Cheongpung had grown up alone with his grandfather in the mountains from an age he couldn’t even remember.

Whatever his grandfather told him, he must have simply accepted it.

“Cranes don’t bring babies? Then am I not my grandfather’s grandson?”

“Well, that’s…”

I continued with a heavy heart. Cheongpung was twenty years old, and now that he had come down from the mountains, it was time for him to learn about the world one thing at a time.

“There are three stages involved in having a child: ovulation, fertilization, and implantation. Try it.”

“With Benefactor?”

“Why would you do it with me? Are you insane? I said to repeat the words out loud.”

“Yes. Ovulation, fertilization, implantation…”

However, the sex education I had begun so ambitiously had to end the moment it started.

“You bloody little bastards! How dare you behave like this in front of a great Senior of Murim!”

The owner of that growling voice was, of course, Gong Ilhyuk.

With help from the other two men officially known as the Three Hands of Zhongnan—but more accurately described as his lackeys—he had even had a splint attached. Now he glared at us.

“A frontier bumpkin and a fool who acts tough because he trusts only his strength dare look down on a disciple of the great Zhongnan Sect?”

Cheongpung’s eyes went round.

“Am I the fool?”

“Probably.”

“Then Benefactor is the frontier bumpkin?”

“Thank you very much for telling me.”

I let out a deep sigh. This man was old enough to know better, yet he still seemed unable to understand the situation. Was his background as a member of the Zhongnan Sect, and his faith in his father’s cousin, simply too strong?

“Well, our Senior sure has a loose mouth.”

“What did you say?”

“Never mind me. What are you going to do if what this friend said is true?”

“If it were true, there’s no way Li Feng wouldn’t have recognized him.”

Li Feng? Why was Li Feng being mentioned here?

I looked at Li Feng, puzzled. He had gone rigid as though he had seen a ghost, but now he finally parted his lips.

“I am a lay disciple of Huashan. Until ten years ago, I was at the main sect.”

Gong Ilhyuk added with a mocking grin,

“That fellow was quite prominent among the lay disciples. At least, until he lost to me during a friendly duel with our sect. Isn’t that right?”

“That’s correct. I stayed at the Zhongnan Sect for two days for the duel, but I ate something bad and became seriously ill.”

“That story again. Don’t you ever get tired of it?”

“Isn’t it a strange coincidence, no matter how often I think about it? Everyone who was scheduled to duel with you, myself included, suffered the same fate.”

“……So you still can’t accept your defeat?”

“No. I accepted it a long time ago. In fact, thanks to you, I learned what Murim was like. As tuition, it was a cheap lesson.”

Gong Ilhyuk’s eyebrow twitched at Li Feng’s calm tone.

“Enough pretending to be magnanimous. Answer me honestly. Have you ever seen that fool at Huashan?”

“Before that, let me ask you one thing. Do you still think I left Huashan because of you?”

“Of course. You ran out of Huashan less than two months after our duel. What excuse are you going to make now?”

“It’s true that I was discouraged for a while… but you’re wrong.”

Li Feng shook his head and continued slowly.

“It had been about a month since that day. My Master suddenly told me that there was somewhere we had to go. When we arrived, all the leaders of our sect, including the Sect Leader, were gathered there.”

“Did they hold a consolation banquet for a lay disciple? Huashan is more generous than I thought.”

“It is a generous sect. After all, they let a failure like me join them on an important visit to see our Grandmaster.”

Gong Ilhyuk’s eyes narrowed.

“Your Grandmaster? Could it be…?”

“There is only one Grandmaster in our sect. Sword Saint Mae Jonghak. The one everyone knows.”

Gasps rose from several places around the hall. Meanwhile, growing unease spread across Gong Ilhyuk’s face.

“That’s impossible. I heard the Sword Saint hadn’t shown himself in a long time…”

“It’s true. However, he was still living at Huashan. He had simply gone into such deep seclusion that we hadn’t been able to find him.”

“Th-Then what happened?”

“We combed through Huashan from top to bottom. We had to break through ten formations before we could reach his residence. Can you guess what I saw there?”

Everyone present could guess. Li Feng’s gaze was fixed on Cheongpung’s face.

“A cute little boy. He was much smaller than the other children his age, but he was diligently swinging a sword… No one could laugh. Who could laugh after seeing a monster perform the Plum Blossom Sword Technique at the age of ten?”

“……!”

“……!”

Silent shock spread through the crowd. Gong Ilhyuk stammered.

“That—that’s impossible. As far as I know, one must be at least First Rate to perform the Plum Blossom Sword Technique…”

“Unimaginable things sometimes happen in Murim. Compared to that, pulling dirty tricks in a friendly duel is nothing.”

Li Feng gave a self-deprecating laugh.

“After more than a month of facing the wall in training, I came to a realization. I had no reason to remain there. That was why I left Huashan. What do you think? Isn’t it interesting?”

The story Li Feng told had a powerful impact. Everyone, myself included, stared silently at Cheongpung.

Suddenly, I remembered the conversation I had shared with him at Honghwa Inn the night before.

*“I was ten years old. One day, dozens of people came barging in and made a scene. I remember my grandfather shouting at them to get the hell out before he set fire to the mountain.”*

*“Ah. So that’s why he keeps changing where he lives…?”*

*“Yes. Fortunately, the mountain is so large that he’s managed to avoid them for ten years.”*

Until then, I hadn’t known that the people who had come to cause trouble ten years ago were the leaders of Huashan, or that the Sword Saint Mae Jonghak was Cheongpung’s grandfather.

And the part about them making a scene was only how it had appeared from young Cheongpung’s perspective. The reality had probably been very different.

*Who would cause trouble with the Sword Saint? That’s a perfect way to get yourself killed.*

The Sword Saint who had threatened to set fire to his own sect wasn’t exactly ordinary, either.

In any case, on the day Huashan had nearly become a real volcano, Li Feng had met Cheongpung as a child and clearly despaired after witnessing his talent.

*Fair enough. First Rate at the age of ten.*

There were countless people who couldn’t reach First Rate even after turning twenty.

Two of the rising martial artists from the Five Gates of Shanxi present here still weren’t quite good enough to be called First Rate masters.

And yet Cheongpung had reached that realm at the age of ten.

*Could Jin Mukyung have done the same?*

The moment that question occurred to me, Gong Ilhyuk shouted as though suffering a fit.

“Proof! What proof is there that he’s that child?”

The rising martial artists of the Five Gates of Shanxi who had been trying desperately to curry favor, Hong Jin, who had been watching with great interest, and even the other two members of the Three Hands of Zhongnan all frowned as though they had planned it together.

“There’s no proof. All I have is my memory.”

“Exactly. Mountains and rivers change in ten years. Should I really trust your paltry memory?”

“No. To be honest, I’m not certain either. I don’t know how that child grew up.”

Li Feng answered calmly, then suddenly drew his sword.

*Shing.*

He studied the blade, which radiated a cold chill, and asked Cheongpung,

“Young Hero. How much do you know about Huashan’s martial arts?”

Cheongpung answered with a bewildered expression.

“Uh, I’m not from Huashan.”

“You’re not from Huashan…”

“Yes. My grandfather just taught me various things, saying they would be good to learn.”

“Then allow me to ask you something. Of the Six Harmonies Sword, Plum Blossom Sword Technique, Supreme Clarity Sword, Taeeul Miri Palm, Falling Flower Chasing Shadow Palm, and Scattering Flowers Shadowless Hand… how many do you know?”

“All of them.”

“Heh. All of them. Every one.”

Li Feng gave a hollow laugh and handed the sword he was holding to Cheongpung.

“Could you perform the Plum Blossom Sword Technique?”

“My grandfather told me not to show my martial arts to anyone.”

“One form—or rather, a single sword stroke—will be enough.”

After hesitating for a moment, Cheongpung took hold of the hilt.

“Then I’ll show you briefly.”

The instant he finished speaking, something changed.

*Sssssss.*

*Sword Energy? No.*

From Cheongpung’s head to his toes, tangible strands of purple qi flowed from his entire body.

It was Extreme Yang internal energy so potent that merely being near it scorched the breath in one’s lungs.

“Zaha Divine Technique[^2]…!”

Li Feng let out a cry of delight.

At that moment—

*Whoosh!*

The tip of Cheongpung’s sword traced a beautiful arc.

Like plum blossoms falling at the end of the season, a single streak of Sword Energy cleaved the enormous table in half.

The food, the dishes, even the sturdy table.

“Ah…”

A gasp escaped me before I knew it.

Breaking things was easy. But Cheongpung’s Sword Energy was so sharp and clean that, if the table hadn’t collapsed a moment later, no one would have noticed it had been cut.

*Boom! Crash!*

As the table split in two and collapsed, Li Feng clasped his fist and palm in an exceedingly respectful salute.

“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

[^1]: Candied hawthorn skewers are fruit skewers coated in hardened sugar.

[^2]: A Huashan internal-energy technique.
```
